

LFC - Language from context
---------------------------


Objective

help people learn new languages.

Steps:

1. determine language proficiency
2. send daily email with short text,
   tailored to the proficiency


Language proficiency Assessment
-------------------------------

Via a quiz or a short form where the
user indicates which words are known
and which are unknown, we can make a 
mental model of what are the things 
the student knows and what they don't.

This can be a long form of words
or we may have to figure out a better
way of assessing knowledge of the 
language.

Daily Email Delivery
--------------------
The system sends email to the users
with the words the system assumes are 
known being 95% of the contents of
the email and 5% of words which are
supposed to be unknown.

The unknown words can be added in a 
short vocabulary list at the bottom
of the email. Including their 
definition in the target language and
the translation to the student's 
language

The system selects articles or 
paragraphs from a list of existing
content or perhaps news content,
this content is used as a source
of information, and the system,
selects only content that matches
the criteria.
The system needs a word index 
that can match a given article
to a list of words, this word 
index contains a connection between
articles and words, and after the
index is created, the system
finds articles where 95% of the
words in the article are known
to a given student.

Each student is a record on the
database, and for each student,
a list of known words are stored.

The words are also ranked by how
common they are, so that more common
words are put on top of the results.

This is so that the student learns
the most common words first, and
later proceeds to learn less common
words.

Assuming enough content is found,
the system could categorize the
source article database and find
the correct articles in each case.

The email contains a link to a 
open platform where the user can
indicate which words are known and
which words are not known, so 
the users can train the system
constantly regarding newly acquired
words that may have originated
from external sources during
the process.


The user interface is simple, and
lets users indicate words by
clicking on words they don't know.

# System Entities
## Language
  + languageId
  + languageName

## Word
  + languageId
  + WordId
  + word
  + index
  + category (grammar, vocab, etc).

## Translation
  + sourceLanguageId
  + destinationLanguageId
  + sourceWordId
  + translationText

## Definition
  + languageId
  + wordId
  + definitionText

## Article
  + ArticleId
  + title
  + contents
  + length (words)
  - wordsDefinedBy()
	 (This returns which words are defined by this article)

## ArticleDefinition
  + articleId
  + wordId

## WordIndex
  + wordId
  + articleId
  - buildIndex()
	(build an index of all words
	 from all articles for fast checking)

## Student
  + studentId
  + Name
  + level (begginner, intermediate, advanced=
  + Email
  + FBID
  + desiredKGrowth
  + active
  + sourceLanguageId
  - sendMessage(title, body)
  - getAllStudents()
  - createNewStudent(name,level,email,fbid,kgrowth)
  - unsuscribeStudent(email)
	(users should be able to unsuscribe at any time)
  - setDesiredGrowth(email, growth)
	users can indicate how /fast/ they want to learn.
  - markWordAsKnown(email, word)
	the user clicks on word to indicate they know them
	as a result the system will assume knowledge of new words
	these words *may* have come from the list
	of new vocabulary or from any where in the article.
  - getGrowthGraph(email, dateStart,dateEnd)
	the system can know how many new words are being
	acquired by a student in a given period.

## Target
 + targetId
 + studentId
 + languageId
 + sourceLanguageId
 - suscribeToDailyMessage(source, dest, email)


## Knowledge
  + studentId
  + wordId
  + dateLearned
  - showStudentKnowledgeForm()
	(shows a form to a student so he can
	indicate what he knows and what he doesn't)

## Message
  + messageId
  + languageId
  + studentId
  + timestamp
  + title
  + body
  + kgrowth
  - calculateKGrowth()
	calculates how many words are actually unknown
	in the message and returns a number from 0% to 100%
  - getMessageVocabularyTable(title, body)
	builds a vocabulary table of words which are supposed
	to be unknown to the student from the contents
	of the article and uses as a 
  - sendAllMessages()
	sends a message to all students,
	this can be run as a cron job.
  - sendMonthlyReport()
	sends a montly report to all students with knowledge
	acquisition information so they can visualize the progress
	email includes a graph and a list of words.

  - getMessageTemplate()
	returns the template for the email format
  - showMessageOnline(messageId)
	shows a message online
	so students can click on it



