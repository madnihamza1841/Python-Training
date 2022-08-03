Task Description
=======

Build a Typing Tester. This should show the user some text, and then challenge them to type it, timing them for the length of time it takes them to finish and scoring them on their accuracy.

## Acceptance Criteria:
1. Sign up on RapidAPI(https://rapidapi.com/)
2. Use this Dictionary API ( https://rapidapi.com/mcnaveen/api/random-words-with-pronunciation ) to get random words
3. Timer should start as soon as the word is displayed on screen
4. Timer should measure the amount of time it takes for the user to type the word
5. User must press ‘enter’ after typing the word to submit their answer
6. Misspelling should have a score penalty
7. Backspace should be allowed but should have a score penalty
8. Case sensitivity should be accounted for
9. Upon submission, the output should include pronunciation and definition of the word(data is included in API response) along with the score for that spelling.
10. Output should show the negative points awarded for misspelling/backspace

## Notes:
1. Use appropriate modules for hitting the API endpoint and recording keyboard clicks. 
2. Give preference to standard python libraries where possible. Divide the program into modules.

## Scoring system:
Check score by comparing every letter inputted by the user against the word’s letters. Score will consist of two equal parts. The accuracy of the typed word will have 50% weightage, it will be termed as the accuracy score. The time to type the word will also have 50% weightage. It will be termed as the time score.

### Formula to calculate accuracy score:
1. score of one letter = 100/total letters in the word 
2. penalty for 1 backspace = score of one letter 
3. penalty for 1 wrong letter = score of one letter

#### Target time to type a word:
1. Avg. time it takes to hover hands from mouse to keyboard or vice versa = 0.4s
2. Avg. time it takes a normal typist for one keystroke = 0.28s

#### Formula to calculate time score:
Raw score = (Time taken to type the word/0.4s + (0.28s * no. of letters + 1))
If the raw score is less than 1, the final score should be full (100). If raw score is greater than 1, then: final score: 100 / raw score.Final score should not go below 0, if it does then award 0 points for time score

## Sample output:
Word: Intellectualism 
No. of letters: 15

User typed: intellectualism 
Time taken by the user: 5s

Accuracy score: 86.67 
Time score: 98

Total score: 92.33

Definition: Belief that all knowledge is derived from reason 
Pronunciation: Intelektualism

