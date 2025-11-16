from flask import Flask, render_template, request, jsonify
from chatbot_core import Chatbot
from config import Config


app = Flask(__name__)
app.config.from_object(Config)

chatbot = Chatbot()

def initialize_chatbot():
    """Initialize chatbot"""
    if not chatbot.initialize():
        print("WARNING: Failed to initialize chatbot")


@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({
                'success': False,
                'message': 'No message provided'
            }), 400
        
        response = chatbot.process_message(user_message)
        
        return jsonify(response)
        
    except Exception as e:
        print(f"Chat error: {str(e)}")
        return jsonify({
            'success': False,
            'message': f'Server error: {str(e)}'
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'database_connected': chatbot.is_connected
    })


if __name__ == '__main__':
    initialize_chatbot()
    app.run(host='0.0.0.0', port=5000, debug=Config.DEBUG)
