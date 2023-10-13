from ftplib import *
ftp_ativo=False
ftp = FTP('ftp.ibiblio.org')
print(ftp.getwelcome())
ftp.quit()