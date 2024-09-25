import random
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from konlpy.tag import Okt
import os

all_parts_of_speech = ['명사', '동사', '형용사', '부사', '접속사', '대명사', '관형사', '전치사', '감탄사', '조사']

if __name__ == "__main__":
    
    name = input("학생 이름을 입력해주세요: ")
    grade = input("학생 학년을 입력해주세요: ")
    user_id = name + " - " + grade+"학년"  

    difficulty = input("난이도를 선택하세요 (1: 쉬움, 2: 어려움): ")
    
    question_bank = []
    sampled_questions = random.sample(question_data, 10)  

    quiz = QuizBrain(question_bank, user_id)

    for question in sampled_questions:
        question_info = quiz.generate_grammar_questions(question)
        if question_info:
            question_bank.append(Question(question_info["text"], question_info["answer"], question_info["original_sentence"]))

    for _ in range(len(quiz.question_list)):
        current_question = quiz.question_list[quiz.question_number]


        print(f"문장: {current_question.original_sentence}")

        if difficulty == '1':  # 쉬움
            correct_answer = current_question.answer
            
            incorrect_answers_pool = [pos for pos in all_parts_of_speech if pos != correct_answer]
            incorrect_answers = random.sample(incorrect_answers_pool, 4)

            choices = [correct_answer] + incorrect_answers  
            random.shuffle(choices)  

            print("가능한 답변: ", ', '.join(choices))  
            user_answer = input(f"Q{quiz.question_number + 1}: {current_question.text}\n품사를 입력하세요: ")
            quiz.check_answer(user_answer, current_question.answer, time_taken=0, question_text=current_question.text)
            quiz.next_question()  

        elif difficulty == '2':  # 어려움
            user_answer = input(f"Q{quiz.question_number + 1}: {current_question.text}\n품사를 입력하세요: ")
            quiz.check_answer(user_answer, current_question.answer, time_taken=0, question_text=current_question.text)
            quiz.next_question()  


    if quiz.logs:
        quiz.save_logs_to_db()

    quiz.close_connection()  

    print("문제 풀이가 완료되었습니다")
    print(f"최종 점수: {quiz.score}/{quiz.question_number}")

