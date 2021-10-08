# import sqlite3 as sql
# password = sql.connect('password.db')
password = {}

def buat_():
    nama = input('masukkan Nama: ')
    password1 = input('masukkan Password: ')
    password2 = input('Ulangi masukkan Password: ')
    return nama, password1, password2

def buat_pass():
    nama, password1, password2 = buat_()
    while password1 != password2:
        print('ulangi buat password...')
        nama, password1, password2 = buat_()
        if password1 == password2:
            password[nama] = password1
            print(password)
            break;
    else:
        password[nama] = password1
        print(password)
        main_()

def ulangi():
    buat_pass()

def main_():
    print('########### This is Password Generation ###########')
    print('(1) to show password')
    lam = int(input('Your Choice: '))
    if lam == 1:
        name = input('whats password?')
        show_password(name)
    else:
        pass

def show_password(whatpass=None):
    try:
        x = password[whatpass]
        print('Your {} password is: {}'.format(whatpass, x))
        # lanjut()
    except:
        argue = input('Belum ada password, mau buat? "Y/N" (Y):')
        if ((argue == 'Y') or (argue == 'y') or (argue == '')):
            print('lanjut buat password')
            buat_pass()
        else:
            print('argue salah')

def lanjut():
    lanjutkah = input('lanjut? "Y/N" (Y)')
    if (lanjutkah == 'Y') or (lanjutkah == 'y') or (lanjutkah == ''):
        main_()
    else:
        pass

main_()
