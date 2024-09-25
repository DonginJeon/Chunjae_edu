import random
import tkinter as tk
from tkinter import messagebox
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import time

all_parts_of_speech = ['명사', '동사', '형용사', '부사', '접속사', '대명사', '관형사', '전치사', '감탄사', '조사']

class GrammarQuizApp:
    def __init__(self, master):
        self.master = master
        self.master.title("문법 문제 맞추기 퀴즈")
        self.master.geometry("500x600")

        self.user_id = ""
        self.quiz = None
        self.current_question = None
        self.start_time = None

        self.create_widgets()

    def create_widgets(self):
        # 학생 이름 입력
        self.name_label = tk.Label(self.master, text="학생 이름을 입력해주세요:")
        self.name_label.pack()

        self.name_entry = tk.Entry(self.master)
        self.name_entry.pack()

        # 학생 학년 입력
        self.grade_label = tk.Label(self.master, text="학생 학년을 입력해주세요:")
        self.grade_label.pack()

        self.grade_entry = tk.Entry(self.master)
        self.grade_entry.pack()

        # 난이도 선택
        self.difficulty_label = tk.Label(self.master, text="난이도를 선택하세요 (1: 쉬움, 2: 어려움):")
        self.difficulty_label.pack()

        self.difficulty_var = tk.StringVar(value='1')  # 기본값 '1'으로 설정
        self.difficulty_easy = tk.Radiobutton(self.master, text="쉬움", variable=self.difficulty_var, value='1')
        self.difficulty_easy.pack()
        self.difficulty_hard = tk.Radiobutton(self.master, text="어려움", variable=self.difficulty_var, value='2')
        self.difficulty_hard.pack()

        # 퀴즈 시작 버튼
        self.start_button = tk.Button(self.master, text="퀴즈 시작", command=self.start_quiz)
        self.start_button.pack(pady=10)

        # 질문 표시
        self.question_label = tk.Label(self.master, text="", wraplength=400)
        self.question_label.pack(pady=20)

        # 답변 입력
        self.answer_entry = tk.Entry(self.master, width=50)
        self.answer_entry.pack(pady=10)

        # 제출 버튼
        self.submit_button = tk.Button(self.master, text="제출", command=self.submit_answer)
        self.submit_button.pack(pady=5)

        # 결과 및 타이머 표시
        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=20)

        # 출력창
        self.output_text = tk.Text(self.master, wrap=tk.WORD, height=10, width=50)
        self.output_text.pack(pady=10)

        # 타이머
        self.timer_label = tk.Label(self.master, text="소요 시간: 0초")
        self.timer_label.pack()

    def start_quiz(self):
        name = self.name_entry.get()
        grade = self.grade_entry.get()
        self.user_id = f"{name} - {grade}학년"

        question_bank = []
        sampled_questions = random.sample(question_data, 10)

        self.quiz = QuizBrain(question_bank, self.user_id)

        for question in sampled_questions:
            question_info = self.quiz.generate_grammar_questions(question)
            if question_info:
                question_bank.append(Question(question_info["text"], question_info["answer"], question_info["original_sentence"]))

        self.start_time = time.time()  # 시작 시간 기록
        self.next_question()

    def next_question(self):
        if self.quiz.question_number < len(self.quiz.question_list):
            self.current_question = self.quiz.question_list[self.quiz.question_number]
            self.question_label.config(text=f"문장: {self.current_question.original_sentence}")
            self.result_label.config(text="")
            self.answer_entry.delete(0, tk.END)
            self.output_text.delete(1.0, tk.END)  # 이전 출력 지우기
            self.output_text.insert(tk.END, f"Q{self.quiz.question_number + 1}: {self.current_question.text}\n")

            # 쉬움 난이도일 경우 가능한 선택지를 출력
            if self.difficulty_var.get() == '1':
                correct_answer = self.current_question.answer
                incorrect_answers_pool = [pos for pos in all_parts_of_speech if pos != correct_answer]
                incorrect_answers = random.sample(incorrect_answers_pool, 4)

                choices = [correct_answer] + incorrect_answers  
                random.shuffle(choices)
                choices_text = "가능한 답변: " + ', '.join(choices)
                self.output_text.insert(tk.END, choices_text + "\n")

        else:
            elapsed_time = int(time.time() - self.start_time)
            messagebox.showinfo("퀴즈 완료", f"모든 문제가 완료되었습니다!\n최종 점수: {self.quiz.score}/{self.quiz.question_number}\n소요 시간: {elapsed_time}초")
            self.master.quit()

    def submit_answer(self):
        user_answer = self.answer_entry.get()
        if self.difficulty_var.get() == '1':  # 쉬움
            correct_answer = self.current_question.answer
            self.quiz.check_answer(user_answer, correct_answer, time_taken=0, question_text=self.current_question.text)

            if user_answer == correct_answer:
                result_text = f"정답: {correct_answer} - 정답입니다!"
            else:
                result_text = f"정답: {correct_answer} - 틀렸습니다!"

            self.output_text.insert(tk.END, result_text + "\n\n")  # 한 줄 띄우기
        else:  # 어려움
            self.quiz.check_answer(user_answer, self.current_question.answer, time_taken=0, question_text=self.current_question.text)

            if user_answer == self.current_question.answer:
                result_text = f"정답: {self.current_question.answer} - 정답입니다!"
            else:
                result_text = f"정답: {self.current_question.answer} - 틀렸습니다!"

            self.output_text.insert(tk.END, result_text + "\n\n")  # 한 줄 띄우기
        
        self.next_question()

    def update_timer(self):
        elapsed_time = int(time.time() - self.start_time)
        self.timer_label.config(text=f"소요 시간: {elapsed_time}초")
        self.master.after(1000, self.update_timer)  # 1초마다 타이머 업데이트

if __name__ == "__main__":
    root = tk.Tk()
    app = GrammarQuizApp(root)
    root.mainloop()
