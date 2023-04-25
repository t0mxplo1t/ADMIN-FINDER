import requests

d = "\033[0m"

def banner():
	print("""\033[36m
 █████╗ ██████╗ ███╗   ███╗██╗███╗   ██╗      ███████╗██╗███╗   ██╗██████╗ ███████╗██████╗
██╔══██╗██╔══██╗████╗ ████║██║████╗  ██║      ██╔════╝██║████╗  ██║██╔══██╗██╔════╝██╔══██╗
███████║██║  ██║██╔████╔██║██║██╔██╗ ██║█████╗█████╗  ██║██╔██╗ ██║██║  ██║█████╗  ██████╔╝
██╔══██║██║  ██║██║╚██╔╝██║██║██║╚██╗██║╚════╝██╔══╝  ██║██║╚██╗██║██║  ██║██╔══╝  ██╔══██╗
██║  ██║██████╔╝██║ ╚═╝ ██║██║██║ ╚████║      ██║     ██║██║ ╚████║██████╔╝███████╗██║  ██║
╚═╝  ╚═╝╚═════╝ ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝      ╚═╝     ╚═╝╚═╝  ╚═══╝╚═════╝ ╚══════╝╚═╝  ╚═╝\033[0m
\033[30;43m Simple Admin Finder is written using Python \033[0m\n""")
banner()

target_url = input("\033[1;36mEnter Website : \033[0m")
admin = [
	"admin"
	"admin.php",
	"wp-admin",
	"admin/login.php",
	"login",
	"login.php",
	"administrator",
	"user",
	"dashboard",
	"admin/index.php",
	"moderator",
	"users",
	"wp-login.php",
	"dashboard/index.php",
	"user.php",
	"login_db",
	"account.php",
	"account",
	"admin/account.php",
	"admin/admin",
	"admin/admin.php",
	"adminarea",
	"admin_area/login.php",
	"admin/cpanel.php",
	"admin/dashboard.php",
	"administrator/login.php"
	"admin_login.php",
	"admin/moderator.php",
	"adminpanel.php",
	"admin/upload.php",
	"db/admin.php"
]

for adm in admin:
	j = target_url+adm
	res = requests.get(j)
	if res.status_code == 200:
		print("\033[1;32mFound\033[33m",res.status_code,d+target_url+adm)
	else:
		print("\033[1;31mNot Found\033[33m",res.status_code,d+target_url+adm)
