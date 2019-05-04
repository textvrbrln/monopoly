from flask import render_template
from app import app
from app.dice import throw_dice, move_forward

@app.route('/')
@app.route('/index')
def index():
    dice = throw_dice()
    dice_result = {'dice': dice}
    
    go_to_field = move_forward()
    field_result = {'go_to_field': go_to_field}
    
    user = {'username': 'Kris'}
    return render_template('index.html', title='Home', user=user, dice_result=dice_result, field_result=field_result)
