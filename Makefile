all:
	sudo systemctl stop server
	sudo systemctl daemon-reload
	sudo cp server.py /usr/bin/server.py
	sudo chmod +x /usr/bin/server.py
	sudo systemctl start server
	sudo systemctl status server
