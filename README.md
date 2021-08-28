# AMI_description
Lista as propriedades de uma AMI AWS

Integrantes: André Rodrigues / Alexandre / Anderson / Roberto (Bob) / Mauro

VERSÕES

Version_Lambda_S3Bucket_CSV >> código para executar em AWS Lambda, gera o resultado em um arquivo csv para um S3 Bucket.

Version_Local_HardDrive_CSV >> código para executar localmente (notebook), gera o resultado em um arquivo csv dentro do seu hard drive local.

Version_Local_S3Bucket_CSV >> código para executar localmente (notebook), gera o resultado em um arquivo csv para um S3 Bucket.

Version_Local_HardDrive_JSON >> código para executar localmente (notebook), gera o resultado em um arquivo json dentro do seu hard drive local.

INSTRUÇÕES

Version_Lambda_S3Bucket_CSV >>

Alterar o código e inserir o nome do bucket onde o csv deve ser gerado. A role da lambda deve ter permissões para ler as EC2 e escrita no bucket de destino.

Version_Local_HardDrive_CSV >>

Importar os módulos boto3 e csv. A conta que vai executar o código precisa de permissões para ler as EC2 e gravar localmente.

Version_Local_S3Bucket_CSV >>

Importar os módulos boto3 e csv. Alterar o código e inserir o nome do bucket onde o csv deve ser gerado A conta que vai executar o código precisa de permissões para ler as EC2 e escrita no bucket de destino.

Version_Local_HardDrive_JSON >>

Importar os módulos boto3, csv e json. A conta que vai executar o código precisa de permissões para ler as EC2 e gravar localmente.



