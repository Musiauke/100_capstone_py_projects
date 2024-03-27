import pandas as pd
import turtle



screen = turtle.Screen()
screen.title('U.S. States Game')
image = '/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

file_path = '/50_states.csv'

data = pd.read_csv(file_path)
data_list = data.to_dict('records')

guessed_states = []

def display_text(message, x,y):
    text_turtle = turtle.Turtle()
    text_turtle.hideturtle()
    text_turtle.penup()
    text_turtle.goto(x,y)
    text_turtle.write(message, align='center', font=('Arial', 8, 'normal'))


while len(guessed_states) < 50:
    
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States guessed ', prompt ='What is another state name?').title()

   

    if answer_state == 'Exit':
        break

    for item in data_list:
        if answer_state == item['state'] and answer_state not in guessed_states:
            display_text(answer_state, int(item['x'  ]), int(item['y']))
            guessed_states.append(answer_state)
            break


df = pd.DataFrame(guessed_states, columns=['State'])
df.to_csv('/states.csv', index=False)

screen.exitonclick()

