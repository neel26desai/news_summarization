Objective
-
In this project, we set out to use LLMs and NLP to take new articles and summarize them. 
This repo has the code to fine-tune t5-small model and push it to hugging face, and a flask server that can use the deployed model to run our application.

Files in the repo:
1. SummarizationHuggingFace_Training.ipynb - contains the code to get the training dataset, fine tune the T5-small model and push the new model to a hugging face repo.
2. server.py - a flask simple flask app, that receives new articles, uses the model to summarize the article and returns the summary (inference)
3. requirements.txt - the required packages needed for running the inference file
4. Dockerfile - creating a docker image to run server.py, needed when you want to deploy the model on Azure VM
5. project_ui/app.py - Flask app, which the user uses for consuming the model
6. project_ui/template - contains the html file for user interface
7. project_ui/invoke_custom.py - simple logic for testing the server.py, can test both local and Azure deployment.


Reference:
1. https://www.analyticsvidhya.com/blog/2023/07/build-a-text-summariser-using-llms-with-hugging-face/

2. https://huggingface.co/docs/transformers/tasks/summarization

3. https://colab.research.google.com/github/huggingface/notebooks/blob/main/transformers_doc/en/pytorch/summarization.ipynb#scrollTo=DbMeitm3wpiF
