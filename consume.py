from zeep import Client 

cliente=Client(
 'https://www.dataaccess.com/webservicesser/NumberConversion.wso?WSDL'    
)

result =Client.service.NumberToWords(5)
print(result)