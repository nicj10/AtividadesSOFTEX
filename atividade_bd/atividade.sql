-- 1. Mostre todos os registros da tabela Aluno. 
SELECT * FROM Aluno

-- 2. Exiba apenas o nome e a nota1 de todos os alunos.
SELECT nome, nota1 FROM Aluno

-- 3.  Liste todos os alunos cuja nota2 seja maior que 8.
SELECT nome, nota2 FROM Aluno
WHERE nota2 > 8 

-- 4. Mostre os alunos que nasceram após o ano de 2000.
SELECT nome, data_nascimento
FROM Aluno
WHERE data_nascimento > '2000-01-01';

-- 5. Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.
SELECT nome, mensalidade FROM Curso 
WHERE mensalidade > 600

-- 6. Mostre o nome das turmas e o ano correspondente, ordenados pelo ano em ordem crescente.
SELECT nome, ano FROM Turma
ORDER BY ano;

-- 7. Liste o ano das turmas e a quantidade de turmas por ano.
SELECT ano, COUNT(*) AS turmas 
FROM Turma
GROUP BY ano

-- 8. Calcule a média da nota1 dos alunos por turma_id.
SELECT AVG(nota1) AS Média, id_turma FROM aluno
GROUP BY id_turma


-- 9.  Mostre o ano e a quantidade de turmas apenas para os anos que têm mais de 2 turmas.
SELECT ano, COUNT(*) AS quantidade_turmas
FROM Turma
GROUP BY ano
HAVING COUNT(*) > 2;


-- 10. Exiba o nome dos cursos e suas mensalidades, ordenando primeiro pela mensalidade (decrescente).
SELECT nome, mensalidade
FROM Curso 
ORDER BY mensalidade DESC;