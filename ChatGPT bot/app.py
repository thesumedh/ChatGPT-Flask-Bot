from flask import Flask, render_template, request, jsonify 
import openai 


app = Flask(__name__) 

# OpenAI API Key 
openai.api_key = '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'

def get_completion(prompt): 
	print(prompt) 
	query = openai.Completion.create( 
		engine="gpt-3.5-turbo-instruct", 
		prompt=prompt, 
		max_tokens=1024, 
		n=1, 
		stop=None, 
		temperature=0.5, 
	) 

	response = query.choices[0].text 
	return response 

@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
	if request.method == 'POST': 
		print('step1') 
		prompt = request.form['prompt'] 
		response = get_completion(prompt) 
		print(response) 

		return jsonify({'response': response}) 
	return render_template('index.html') 


if __name__ == "__main__": 
	app.run(debug=True) 
