import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from konlpy.tag import Okt
import tkinter as tk
from tkinter import messagebox
from art import display_grammar_game
from study import part_of_speech_explanations

all_parts_of_speech = ['명사', '동사', '형용사', '부사', '접속사', '대명사', '관형사', '전치사', '감탄사', '조사']

class GrammarQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Grammar Quiz")
        self.quiz = None
        self.question_bank = []
        self.incorrect_answers = []
        
        self.create_widgets()

    def create_widgets(self):
        # Title display
        self.title_label = tk.Label(self.master, text="문법 퀴즈", font=("Arial", 24))
        self.title_label.pack(pady=10)

        self.name_label = tk.Label(self.master, text="학생 이름:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        self.grade_label = tk.Label(self.master, text="학생 학년:")
        self.grade_label.pack()
        self.grade_entry = tk.Entry(self.master)
        self.grade_entry.pack()

        self.difficulty_label = tk.Label(self.master, text="난이도를 선택하세요 (1: 쉬움, 2: 어려움):")
        self.difficulty_label.pack()
        self.difficulty_entry = tk.Entry(self.master)
        self.difficulty_entry.pack()

        self.start_button = tk.Button(self.master, text="퀴즈 시작", command=self.start_quiz)
        self.start_button.pack(pady=20)

        self.question_frame = tk.Frame(self.master)
        self.question_label = tk.Label(self.question_frame, text="", font=("Arial", 16))
        self.question_label.pack(pady=10)

        self.answer_entry = tk.Entry(self.question_frame)
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.question_frame, text="제출", command=self.submit_answer)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 16))
        self.result_label.pack(pady=20)

    def start_quiz(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        user_id = f"{name} - {grade}학년"
        difficulty = self.difficulty_entry.get()

        # Prepare the questions
        self.question_bank = random.sample(question_data, 10)
        self.quiz = QuizBrain(self.question_bank, user_id)

        for question in self.question_bank:
            question_info = self.quiz.generate_grammar_questions(question)
            if question_info:
                self.quiz.question_list.append(Question(question_info["text"], question_info["answer"], question_info["original_sentence"]))

        self.question_frame.pack()
        self.next_question()

    def next_question(self):
        if self.quiz.question_number < len(self.quiz.question_list):
            current_question = self.quiz.question_list[self.quiz.question_number]
            self.question_label.config(text=f"문장: {current_question.original_sentence}\n질문: {current_question.text}")

            # Handle answer choices based on difficulty
            if self.difficulty_entry.get() == '1':  # 쉬움
                correct_answer = current_question.answer
                incorrect_answers_pool = [pos for pos in all_parts_of_speech if pos != correct_answer]
                incorrect_answers = random.sample(incorrect_answers_pool, 4)

                choices = [correct_answer] + incorrect_answers
                random.shuffle(choices)

                self.answer_entry.delete(0, tk.END)
                self.answer_entry.insert(0, ', '.join(choices))  # Show options to the user
            else:  # 어려움
                self.answer_entry.delete(0, tk.END)

        else:
            self.end_quiz()

    def submit_answer(self):
        user_answer = self.answer_entry.get().strip()
        current_question = self.quiz.question_list[self.quiz.question_number]

        if not self.quiz.check_answer(user_answer, current_question.answer, time_taken=0, question_text=current_question.text):
            self.incorrect_answers.append(current_question.answer)

        self.quiz.next_question()
        self.next_question()

    def end_quiz(self):
        self.question_frame.pack_forget()
        final_score = self.quiz.score
        total_questions = self.quiz.question_number
        self.result_label.config(text=f"문제 풀이가 완료되었습니다\n최종 점수: {final_score}/{total_questions}")

        # Provide explanations for incorrect answers at the end
        if self.incorrect_answers:
            explanations = "\n틀린 품사에 대한 설명:\n"
            for pos in set(self.incorrect_answers):  # Avoid duplicate explanations
                explanations += f"\n품사: {pos}\n설명: {part_of_speech_explanations.get(pos, '설명이 없습니다.')}\n"
            messagebox.showinfo("틀린 답변 설명", explanations)

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarQuizApp(root)
    root.mainloop()
