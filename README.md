# Password Checker

Nowadays, password hacking is commonplace - which is not surprising at all. According to a recent study, 75% of people don't adhere to password best practices. That means roughly 3 out of 4 people are at risk of having their online accounts compromised. As part of the study, participants were asked why they hadn't taken note of prior warnings, and it was discovered that more than a third of them felt overwhelmed by the prospect of changing their habits. In light of these findings, it seemed to me that a simple solution was needed. Enter, Password Checker. Essentially, it walks users through the process of creating secure passwords. Its accompanying User Interface (UI) isn't fancy, and it was designed without the assumption that its users are tech saavy individuals. It just gets straight to the point, as it should.

![Website screenshot](images/UI-screenshot.png)

## How to Use

First, users are asked to take note of the criteria. They can then begin entering their password, choosing to toggle its visibility by clicking the 'Reveal/Hide Password' button. Once they've input their password, they can click the 'Check Strength' button to determine its strength. They will receive immediate feedback. Depending on whether or not their password meets the specified criteria, they will be informed that their password is either weak, medium or strong. Once they've created a suitable password, they can explore resources which will help them to understand the critical importance of creating secure passwords.

## Features

### Current Features

- First and foremost, it was decided that a UI was needed in order to convey the message in a way that would be appealing to users.

  - Moderate color tones have been used - not too bright and not too dark. Black has also been utilised to create contrast and ensure that all text is clear and easy to read. Additionally, a text glow effect has been added for increased readability.
  - Concise instructions have been included, each section has been clearly marked, and a 'Reveal Password' button has been included, all to aid ease of use.

- When the password checker is utilised, user inputs are passed through a series of logical assessments to determine overall strength. First, the program checks to see if the password is less than 8 characters, if it's a palindrome, and if it contains a date; if any of these conditions return True, the password will be classified as weak. From there, it checks for at least one uppercase letter, one digit, and one special character. If all criteria are met, users will be informed that their password is strong. If only two criteria are met, they will be informed that their password is of medium strength. Finally, if only one criterion has been met, they will be informed that their password is weak.

- A resources section has been added to develop the understanding of users. Many people aren't aware that there are risks to be considered, and so they likely wouldn't think to do any research. By drawing their attention to a series of articles, I'm raising awareness and providing them with relevant information.

### Prospective Features

- Additional password checking criteria, such as penalisation of dictionary words and repeated characters
- Entropy-based calculations to measure password strength more accurately
