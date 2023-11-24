from flask import Flask, render_template, request
from markupsafe import escape
import serial

port1 = 'COM7'
port2 = 'COM5'

ser1_connected = False
ser2_connected = False

try:
  ser1 = serial.Serial(port1, baudrate=9600)
  ser1_connected = True
except:
  print(f"Não foi possível conectar com a {port1}")

try:
  ser2 = serial.Serial(port2, baudrate=9600)
  ser2_connected = True
except:
   print(f"Não foi possível conectar com a {port2}")


app = Flask(__name__)

dc_enable = False
dc_dir = False
vel_dc = '1000'

passo_enable = False
passo_dir = False
vel_passo = '0'

imag_dir_dc = "static/img_hor.png"
imag_en_dc = "static/luz_disable.png"

imag_dir_passo = "static/img_hor.png"
imag_en_passo = "static/luz_disable.png"

@app.route("/")
def index():
  return render_template("index.html")

@app.route('/motor-dc', methods=('GET','POST'))
def motor_dc():
  global dc_enable
  global dc_dir

  global imag_en_dc
  global imag_dir_dc
  global vel_dc
  
  if request.method == 'POST':
      if request.form.get('enable') == 'EN':
          if ser1_connected:
            if ser1.writable():
                if dc_enable:
                  ser1.write(bytes('e\r',encoding='utf-8'))
                  imag_en_dc = "static/luz_enable.png"
                else:
                  ser1.write(bytes('d\r',encoding='utf-8'))
                  imag_en_dc = "static/luz_disable.png"
                dc_enable = False if dc_enable else True


      elif  request.form.get('direction') == 'DIR':
          if ser1_connected:
            if ser1.writable():
                if dc_dir:
                  ser1.write(bytes('a\r',encoding='utf-8'))
                  imag_dir_dc = "static/img_hor.png"
                else:
                  ser1.write(bytes('h\r',encoding='utf-8'))
                  imag_dir_dc = "static/img_anti.png"
                dc_dir = False if dc_dir else True

      else:
          vel_dc = request.form.get('velocity')
          if ser1_connected:
            if ser1.writable():
              ser1.write(bytes(f'v{vel_dc}\r',encoding='utf-8'))


  elif request.method == 'GET':
      return render_template('motor_dc.html', form='form', imgEn=imag_en_dc, imgDir=imag_dir_dc, val_vel = vel_dc)

  return render_template('motor_dc.html',imgEn=imag_en_dc, imgDir=imag_dir_dc, val_vel = vel_dc)


@app.route('/motor-passo', methods=('GET','POST'))
def motor_passo():
    global passo_enable
    global passo_dir

    global imag_en_passo
    global imag_dir_passo
    global vel_passo

    if request.method == 'POST':
        if request.form.get('enable') == 'EN':
            if ser2_connected:
              if ser2.writable():
                  if passo_enable:
                    ser2.write(bytes('e\r',encoding='utf-8'))
                    imag_en_passo = "static/luz_enable.png"
                  else:
                    ser2.write(bytes('d\r',encoding='utf-8'))
                    imag_en_passo = "static/luz_disable.png"
              passo_enable = False if passo_enable else True

        elif  request.form.get('direction') == 'DIR':
            if ser2_connected:
              if ser2.writable():
                  if passo_dir:
                    ser2.write(bytes('a\r',encoding='utf-8'))
                    imag_dir_passo = "static/img_hor.png"
                  else:
                    ser2.write(bytes('h\r',encoding='utf-8'))
                    imag_dir_passo = "static/img_anti.png"
              passo_dir = False if passo_dir else True

        else:
            vel_passo = request.form.get('velocity')
            if ser2_connected:
              if ser2.writable():
                ser2.write(bytes(f'v{vel_passo}\r',encoding='utf-8'))

    elif request.method == 'GET':
        return render_template('motor_passo.html', form='form', imgEn=imag_en_passo, imgDir=imag_dir_passo, val_vel = vel_passo)
    
    return render_template('motor_passo.html', imgEn=imag_en_passo, imgDir=imag_dir_passo, val_vel = vel_passo)



@app.route('/motor-dc/readme')
def readme_dc():
  return render_template('ReadMotorDC.html')

@app.route('/motor-passo/readme')
def readme_passo():
  return render_template('ReadMotorPasso.html')

@app.route('/readme')
def readme():
  return render_template('ReadMe.html')