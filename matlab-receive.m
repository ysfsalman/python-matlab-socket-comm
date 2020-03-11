%%
clear all
clc
port =30000;
while 1
%t = tcpip('localhost', port, 'NetworkRole', 'server');
t = tcpip('0.0.0.0', port, 'NetworkRole', 'server');

i = 0 ;% never listen
count = 0;
fopen(t);
while 1
    if t.BytesAvailable
    data=fread(t, 3, 'int16')
    i = 1;
    count = 0;
    elseif ~t.BytesAvailable && i == 1
        count = count+1;
        if count == 50
        break       
        end
        
    end
    
end
port = port +1;
fclose(t)
end

