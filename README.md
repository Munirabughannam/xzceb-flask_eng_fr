# CHATBOT_ENGLISH_TO_FRENCH
- A server with end points that allows you to translate from English to French and from French to English.

## Project Criteria:

- Use Watson APIs to create Language Translator Service. (1)

- Create an instance of the Language Translator Service in Python code. (1)

- Create a function that translates English to French. (2)

- Create a function that translates French to English. (2)

- Write unit tests to test the above functions. (4)

  - a. assertEqual frenchToEnglish

  - b. assertNotEqual frenchToEnglish

  - c. assertEqual englishToFrench

  - d. assertNotEqual englishToFrench

- Run coding standards check against the functions above. (3)

- Run unit tests and interpret the results. (4)

- Package the above functions and tests as a standard python package. (2)

- Ensure server.py includes code to

  - Import translator.py
  - provide root end point which renders index.html
  - provide end point to translate from French to English
  - provide end point to translate from English to French
- Check the endpoints of the application(2)

  - The endpoint frenchToEnglish works - Translates text as expected

  - The endpoint englishToFrench works - Translates text as expected
