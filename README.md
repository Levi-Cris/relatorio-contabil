<h1>WAF - Laboratório no VirtualBox</h1>

<h2>Descrição</h2>
O projeto consiste em simular um firewall que seria acessado na
web, sendo criado regras de tráfego demonstrando os logs do
sistema e todos os tipos de pacotes que são enviados e
recebidos na rede local além de registrados e codificados com
criptografia para ser repassado ao time de desenvolvimento da
empresa fictícia além de forçar um ataque nas aplicações para
testar a vulnerabilidade
<br />


<h2>Linguagens e Serviços utilizados/VMS:</h2>

- <b>Virtualbox</b> 
- <b>PFSense</b>
- <b>Graylog </b>
- <b>Apache2 </b>
- <b>Burp Suite </b>
- <b>Dirb</b>
- <b>DVWA </b>
- <b>Nmap </b>
- <b>Snort </b>

<h2>Ambientes Usados </h2>

- <b>Windows 11</b>
- <b>Server(Debian 64-bits) </b>
- <b>Graylog(Debian 64-bits) </b>
- <b>WAF(Debian 64-bits) </b>
- <b>Firewall/PFsense (Other Linux 64-bits) </b>
- <b>DVWA (Ubuntu 64-bits) </b>

<h2>Andamento da Aplicação:</h2>

<p align="center">
Ambiente emulado no VirtualBox: <br/>
<img src="https://i.imgur.com/4p7fuQz.png" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Firewall com Regras Nativas do Servidor:  <br/>
<img src="https://i.imgur.com/0SBegvs.jpg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Regras da INTRANET: <br/>
<img src="https://i.imgur.com/C8q94KR.jpg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Regras da DMZ:  <br/>
<img src="https://i.imgur.com/kpCo6Om.jpg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Snort utilizado para regrar:  <br/>
<img src="https://i.imgur.com/XFAJmJs.jpg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Graylog realizando o registro de logs do servidor:  <br/>
<img src="https://i.imgur.com/qPNxPsB.jpg" height="80%" width="80%" alt="Disk Sanitization Steps"/>
<br />
<br />
Aplicação hospedada no servidor pronta para serem realizado os ataques:  <br/>
<img src="https://i.imgur.com/9GeQ5yl.png"/>
<br />
<br />
Máquinas prontas e emuladas para cenário fícticio de ataque:  <br/>
<img src="https://i.imgur.com/YCePYaR.jpg"/>
</p>
