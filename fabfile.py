from fabric import Connection

HOST_IP = "54.165.157.228"
USERNAME = "frank"

def deploy():
    # Simple et efficace : Fabric ira chercher la clé dans /root/.ssh tout seul
    c = Connection(host=HOST_IP, user=USERNAME)
    
    print("--- 1. Installing MySQL ---")
    c.sudo('apt-get update')
    c.sudo('apt-get install -y mysql-server')

    
    print("--- 2. Creating Database 'alu_momo' ---")
    c.sudo('mysql -e "CREATE DATABASE IF NOT EXISTS alu_momo;"')

  
    print("--- 3. Uploading SQL file ---")
    c.put('setup_db.sql', '/tmp/setup_db.sql')


    print("--- 4. Importing Data ---")
    c.sudo('mysql alu_momo < /tmp/setup_db.sql')

    print("--- SUCCESS: Database Deployed on Web-01! ---")

if __name__ == "__main__":
    deploy()
