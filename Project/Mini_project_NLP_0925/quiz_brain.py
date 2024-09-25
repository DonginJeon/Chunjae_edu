import time
from konlpy.tag import Okt
import random
import sqlite3
import os

okt = Okt()

class QuizBrain:
    def __init__(self, q_list, user_id):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0
        self.user_id = user_id
        self.logs = []  

        # 데이터베이스 연결
        self.db_path = 'quiz_logs.db'  # 현재 작업 디렉토리에 저장
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

        # 데이터베이스 테이블 생성
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS quiz_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT,
            question_text TEXT,
            user_answer TEXT,
            correct_answer TEXT,
            is_correct BOOLEAN,
            time_taken TEXT,  -- Change to TEXT if you're adding the "초" suffix
            score INTEGER,
            solved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        ''')

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
  
        start_time = time.time()
        self.question_number += 1


        end_time = time.time()
        time_taken = round(end_time - start_time, 2)



    def check_answer(self, user_answer, correct_answer, time_taken, question_text):
        is_correct = user_answer.lower() == correct_answer.lower()

        if is_correct:
            self.score += 1
            print("정답입니다.")
        else:
            print("오답입니다.")

        print(f"올바른 정답은: {correct_answer}.")
        print(f"당신의 현재 점수는 : {self.score}/{self.question_number}")
        print("\n")

        # 로그를 리스트에 추가
        self.logs.append((question_text, user_answer, correct_answer, is_correct, time_taken))

        # 10문제마다 DB에 저장
        if self.question_number % 10 == 0:
            self.save_logs_to_db()

    def save_logs_to_db(self):
        # 수집된 로그를 데이터베이스에 저장
        for log in self.logs:
            self.cursor.execute('''INSERT INTO quiz_logs (user_id, question_text, user_answer, correct_answer, is_correct, time_taken)
                                  VALUES (?, ?, ?, ?, ?, ?)''',
                                (self.user_id, *log))
        self.conn.commit()
        self.logs.clear()  

    def close_connection(self):
        self.conn.close()
        print("데이터베이스 연결이 종료되었습니다.")

    def generate_grammar_questions(self, sentence):
        parsed_sentence = okt.pos(sentence)  

        questions = []

        for word, pos in parsed_sentence:
            if pos == 'Noun':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "명사", "original_sentence": sentence})
            elif pos == 'Verb':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "동사", "original_sentence": sentence})
            elif pos == 'Adjective':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "형용사", "original_sentence": sentence})
            elif pos == 'Adverb':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "부사", "original_sentence": sentence})
            elif pos == 'Conjunction':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "접속사", "original_sentence": sentence})
            elif pos == 'Pronoun':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "대명사", "original_sentence": sentence})
            elif pos == 'Determiner':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "관형사", "original_sentence": sentence})
            elif pos == 'Preposition':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "전치사", "original_sentence": sentence})
            elif pos == 'Interjection':
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "감탄사", "original_sentence": sentence})
            elif pos == 'Josa':  # Adding 조사
                question = f"문장에서 '{word}'의 품사는 무엇일까요?"
                questions.append({"text": question, "answer": "조사", "original_sentence": sentence})

        if questions:
            return random.choice(questions)
        return None