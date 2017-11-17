import phonebookpkg



if __name__ == "__main__":
    input_type = 'flask'  # console network flask

    if not input_type == 'flask':
        from GUIWrapper import Wrapper
        PhoneBookGUI_ = Wrapper(phonebookpkg.PhoneBookGUI, 'flask')
        while True:
            PhoneBookGUI_.get_operation()
    else:
        from phonebookpkg import phonebook
        from flask import Flask, render_template, request, redirect, session
        phonebook_ = phonebook.PhoneBook()
        app = Flask(__name__)
        app.secret_key = 'sadfm viousgth9'



        @app.route('/', methods=['GET', 'POST'])
        def index():
            message_ = session.pop('message', '')
            return render_template('index.html', message = message_)


        @app.route('/<name>')
        def killAname(name):
            return "Kill a the " + name


        @app.route('/add', methods=['GET', 'POST'])
        def add():
            if not request.method == 'POST':
                return render_template('add.html')
            else:
                name_ = request.form.get('name','')
                phone_ = request.form.get('phone', '')
                message_ = ''
                phone_error_ = ''
                if phone_.isdigit():
                    session['message'] = 'User: ' + name_ + ' / ' + phone_ + ' was added!'
                    return redirect('/')
                else:
                    phone_error_ = 'phone must contain only digits'
                    return render_template('add.html', name = name_ , phone = phone_, message = message_, phone_error = phone_error_ )



        app.run(debug=True)





