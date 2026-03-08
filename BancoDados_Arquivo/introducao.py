"""
Um	banco	de	dados	é	um	arquivo	organizado	para	armazenar	dados.	Muitos	bancos	de
dados	são	organizados	como	um	dicionário,	porque	mapeiam	chaves	a	valores.	A	maior
diferença	entre	um	banco	de	dados	e	um	dicionário	é	que	o	banco	de	dados	está	em	um
disco	(ou	outro	armazenamento	permanente),	portanto	persiste	depois	que	o	programa
termina.
O	módulo	dbm	fornece	uma	interface	para	criar	e	atualizar	arquivos	de	banco	de	dados.
Como	exemplo,	criarei	um	banco	de	dados	que	contém	legendas	de	arquivos	de	imagem.
Abrir	um	banco	de	dados	é	semelhante	à	abertura	de	outros	arquivos:
"""
import dbm

db = dbm.open('banco','c') # C indica que o banco de dados poder ser cirado se não exister

db['img.png'] = 'fotografia'
print(db['img2.png']) #  Quando eu executar este comando ele vai ler o ome do arquivo que foi atribuido
# se a imgem que possui este nome não exister ou estar em outro formato o dbm não irá conseguir ler e vai dar erro

db.close()
