from django.db import models

class Question(models.Model):
    """
    Represents a poll question.

    :ivar question_text: The text of the question.
    :vartype question_text: str
    :ivar pub_date: The date and time the question was published.
    :vartype pub_date: datetime
    """
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        """
        Returns the string representation of the question.

        :return: The text of the question.
        :rtype: str
        """
        return self.question_text


class Choice(models.Model):
    """
    Represents a selectable choice for a poll question.

    :ivar question: The related question this choice belongs to.
    :vartype question: Question
    :ivar choice_text: The text of the choice.
    :vartype choice_text: str
    :ivar votes: The number of votes the choice has received.
    :vartype votes: int
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        """
        Returns the string representation of the choice.

        :return: The text of the choice.
        :rtype: str
        """
        return self.choice_text
