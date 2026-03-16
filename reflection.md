# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- When I first ran the game, it seemed fine from a UI stand point, until I actually played the game, which revealed various glitches. When I tried a value that exceeded the range of 1 to 100, I a message saying go lower, which was the very first error that I noticed. 
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
1. The secret number seemingly kept changing or was out of bounds when I tried edge cases like 0 and 101.
2. The number of available attempts kept changing to random values when I changed the difficulty levels. The number of attempts upon a refresh of the page changes to 7, but it starts at 8 when you play a new game. 
2. When I got the result for a game, I got negative numbers such as -35 and upon a reset of the game, the state did not change, except for the number of attempts. However, I was not allowed to play the game anymore as the buttons did not work. 
---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- I used Copilot and Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- The first copilot suggestion was the fix to the hardcoded range in the info message. Regardless of the difficulty level, it always displays the range of 1 to 100. Copilot was able to successfully implement the fix, but not fully. Now, the ranges were being displayed correctly, but the ranges assigned to the difficulty levels were incorrect, which was not pointed out by Copilot. But on the surface level, the bug was fixed but not entirely.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
- Another suggestion tha copilot made was a fix to a bug regarding even numbered attempts. On even numbered attempts, the AI determined that the secret value was being converted into a string which flawed the comparison logic of the numbers. Its attempt at fixing it was just removing that conversion line all together, which did not fix the problem after I tested the game. The guess value still kept changing and it would randomly go to a low number despite saying go higher. 
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- To check if the bug was actually fixed or not, I did manual tests in the app. I started off with edge cases that would break it right away if the logic was flawed. Then I went on to run at least a handful of tests to determine if the logic was now correct. 
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- One test that I ran manually was using edge cases for the guesses. Since there was no error message in the app, it implies that there is no basic input validation like out of bounds values. Another logic issue I noticed is that ranges themselves for the three difficulties are not correct. So even using pytest, it generated the tests using wrong values that were assigned to the difficulty levels. 
- Did AI help you design or understand any tests? How?
- Yes, AI did help me design tests. One thing it made me realize, however, is that if the underlying logic of my app is still wrong, AI might generate the wrong logic for the tests. So, I ensured that I first checked that the user inputs were validated and then the hints were also correct. 
---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- Based on the code logic, it seemed that each time the user pressed submit, a new random value was generated. If the python script reruns each time the user presses a button and a random value is constantly generated. Hence, the secret is actually never the same value
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- Think of writing notes on a whiteboard. Everytime Streamlit "reruns" all those notes are erased and you start with an empty board. Meaning the state, or the data in the page is constantly refreshed each interaction from the user. Session state fixes this problem by storing data in a session state so that Streamlit had memory of what happened so far. 
- What change did you make that finally gave the game a stable secret number?
- To keep a stable secret number, I stored the secret inside of the session_state and added a guard to prevent changes to it, unless its a new game or the difficulty changes. This approach prevents random values from being generated as the "secret". 
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
- One strategy I learned is how to debug AI slop into code that is readable and maintainable. Restructing was really just a way of making cleaner code with detailed comments that helps the developer understand he logic behind the app. I learned to plan fixes, assess bugs manually, review code logic, and understand that AI can be as good as the prompt I provide it. 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- From now, I will always start on plan mode. Once I idenify the bugs within the code, I will ask AI to plan a fix, Which will allow me to treat it as a fellow engineer proposing a solution. Now, I will be dictating what the AI does instead of letting it refactor or implement code on its own.
- In one or two sentences, describe how this project changed the way you think about AI generated code.
- Through this project, I learned that AI code can be really sloppy if the prompt is weak and naive. But once you know the tools you are working with, the logic of your app, input validation, and best practices, you can use that as context to supercharge your AI's performance. 


