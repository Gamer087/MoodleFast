from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os
import urllib


def text_progres(index,max):
	try:
		if max<1:
			max += 1
		porcent = index / max
		porcent *= 100
		porcent = round(porcent)
		make_text = ''
		index_make = 1
		make_text += '\n['
		while(index_make<21):
			if porcent >= index_make * 5: make_text+='█'
			else: make_text+='░'
			index_make+=1
		make_text += ']\n'
		return make_text
	except Exception as ex:
			return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = '⏬Descargando... \n'
    msg += '📜Nombre del archivo: '+filename+'\n'
    msg += '🔄Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += '📦Total: '+sizeof_fmt(totalBits)+' | Descargado: '+sizeof_fmt(currentBits)+'\n'
    msg += '⚡️Speed: '+sizeof_fmt(speed)+'/s \n'
    msg += '⏰ETA: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    msg = '⏬Descargando...\n'
    msg += '📜Nombre del archivo: '+filename+'\n'
    msg += '🔄Porcentaje: '+str(porcent(currentBits,totalBits))+'%\n'
    msg += '📦Total: '+sizeof_fmt(totalBits)+' | Descargado: '+sizeof_fmt(currentBits)+'\n'
    msg += '⚡️Speed: '+sizeof_fmt(speed)+'/s \n'
    msg += '⏰ETA: '+str(datetime.timedelta(seconds=int(time)))+'s\n\n'

    if tid!='':
        msg+= '/cancel_' + tid
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = '⏫Subiendo...\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📜Nombre:' + str(filename)+'\n'
    msg+= '📦Tamaño Total: ' + str(sizeof_fmt(totalBits))+'| Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '⚡️Speed: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⏰ETA: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    msg = '⏫Subiendo...\n'
    if originalname!='':
        msg = str(msg).replace(filename,originalname)
        msg+= '📜Nombre:' + str(filename)+'\n'
    msg+= '📦Tamaño Total: ' + str(sizeof_fmt(totalBits))+'| Subido: ' + str(sizeof_fmt(currentBits))+'\n'
    msg+= '⚡️Speed: ' + str(sizeof_fmt(speed))+'/s\n'
    msg+= '⏰ETA: ' + str(datetime.timedelta(seconds=int(time))) +'\n'

    return msg
def createCompresing(filename,filesize,splitsize):
    msg = '🗜Comprimiendo... \n\n'
    msg+= '📚Tamaño Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= '🗂Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,split_size,current,count,findex):
    msg = '🏆Finalizado\n'
    msg+= '📜Nombre: ' + str(filename)+'\n'
    msg+= '📦Tamaño Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= '🗃Partes Subidas: ' + str(current) + '/' + str(count) +'\n'
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>🔗ENLACES🔗:</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            msg+= "<a href='"+url+"'>"+f['name']+'</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = '📑Archivos ('+str(len(evfiles))+')\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = '⚙️Panel de Usuario⚙️\n\n'
    msg+= '👤Nombre: @' + str(username)+'\n'
    msg+= '🛃Usuario: ' + str(userdata['moodle_user'])+'\n'
    msg+= '🔐Contraseña: ' + str(userdata['moodle_password']) +'\n'
    msg+= '🌐Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= '🆔RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
    msg+= '☁️Tipo de nube: ' + str(userdata['cloudtype'])+'\n'
    msg+= '📤Tipo de subida: ' + str(userdata['uploadtype'])+'\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= '📁Dir: /' + str(userdata['dir'])+'\n'
    msg+= '📚Tamaño de Zips : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    rename = 'NO'
    if userdata['rename'] == 1:
       rename = 'SI'
    msg+= '📝Rename: ' + rename + '\n'
    shorturl = (userdata['urlshort'] == 1)
    shortener = 'NO'
    if shorturl:
       shortener = 'SI'
    msg += '🔗ShortUrl: ' + shortener + '\n\n'
    msgAdmin = 'NO'
    if isadmin:
        msgAdmin = 'SI'
    msg+= '👮🏻‍♂️Admin: ' + msgAdmin + '\n'
    proxy = 'NO'
    if userdata['proxy'] !='':
       proxy = 'SI'
    msg+= '🧬Proxy: ' + proxy + '\n\n'
    if userdata['moodle_user'] and userdata['moodle_password'] and userdata['moodle_host'] != '':
        msg+= "🗒Use el comando /login para conectar la cuenta🗒"
    return msg