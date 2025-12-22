"""  
Classes:
1. Question (abstract/base class)
2. MCQQuestion
3. ParagraphQuestion
4. Category
5. Topic
6. ExamPortal

"""
    
#Class Topic
class Topic:
    def __init__(self, name: str):
        self.name = name


#Class Category
class Category:
    def __init__(self, name: str):
        self.name = name
        

from abc import ABC, abstractmethod

#Class Question (base/abstract class)
class Question(ABC):
    def __init__(self, qid: int, question: str, category: Category, topic: Topic):
        self.qid = qid
        self.question = question
        self.category = category
        self.topic = topic

    @abstractmethod
    def get_details(self):
        pass


#Class MCQQuestion (child class)
class MCQQuestion(Question):
    def __init__(self, qid, question, category, topic, options, correct_option):
        super().__init__(qid, question, category, topic) #calls the parent class constructor
        self.options = options
        self.correct_option = correct_option

    def get_details(self):
        details = f"MCQ: {self.question}\n"
        for idx, opt in enumerate(self.options, start=1):
            details += f"  {idx}. {opt}\n"
        return details


#CLass ParagraphQuestion
class ParagraphQuestion(Question):
    def __init__(self, qid, question, category, topic, word_limit):
        super().__init__(qid, question, category, topic)
        self.word_limit = word_limit

    def get_details(self):
        return f"Paragraph: {self.question}"

#Class Exam Portal
class ExamPortal:
    def __init__(self):
        self.questions = []

    def add_question(self, question: Question):
        self.questions.append(question)

    # 1. Find total number of questions
    def get_total_questions(self):
        return len(self.questions)

    # 2. List all questions belonging to a topic
    def get_questions_by_topic(self, topic_name: str):
        return [q for q in self.questions if q.topic.name == topic_name] #topic if of type Topic

    # 3. List all questions belonging to a topic and category
    def get_questions_by_topic_and_category(self, topic_name: str, category_name: str):
        return [
            q for q in self.questions
            if q.topic.name == topic_name and q.category.name == category_name #category if of type Category
        ]

     
        
if __name__ == "__main__":
    # Categories
    programming = Category("Programming")
    mathematics = Category("Mathematics")

    # Topics
    python = Topic("Python")
    algebra = Topic("Algebra")

    # Questions
    q1 = MCQQuestion(
        1,
        "What is Python?",
        programming,
        python,
        ["Language", "Snake", "Tool"],
        "Language"
    )

    q2 = ParagraphQuestion(
        2,
        "Explain OOP concepts",
        programming,
        python,
        200
    )

    q3 = MCQQuestion(
        3,
        "Solve x + 5 = 10",
        mathematics,
        algebra,
        ["3", "5", "10"],
        "5"
    )

    # Portal
    portal = ExamPortal()
    portal.add_question(q1)
    portal.add_question(q2)
    portal.add_question(q3)

    print("Total Questions:", portal.get_total_questions())

    print("\nQuestions for topic 'Python':")
    for q in portal.get_questions_by_topic("Python"):
        print("-", q.get_details())

    print("\nQuestions for topic 'Algebra' and category 'Mathematics':")
    for q in portal.get_questions_by_topic_and_category("Algebra", "Mathematics"):
        print("-", q.get_details())
