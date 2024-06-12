from dWo import app
import webview

if __name__ == '__main__':
    app.run(debug=True)
    window = webview.create_window('DevWithOps',app)
    webview.start()
