CREATE TABLE Reservas (
    id_reserva INT PRIMARY KEY AUTO_INCREMENT,
    nome_cliente VARCHAR(100) NOT NULL,
    email_cliente VARCHAR(100),
    telefone_cliente VARCHAR(20),
    data_checkin DATE NOT NULL,
    data_checkout DATE NOT NULL,
    numero_quarto INT NOT NULL,
    total_diarias DECIMAL(10, 2) NOT NULL,
    status_reserva ENUM('Confirmada', 'Cancelada', 'Pendente') NOT NULL
);


INSERT INTO Reservas (nome_cliente, email_cliente, telefone_cliente, data_checkin, data_checkout, numero_quarto, total_diarias, status_reserva)
VALUES
    ('João Silva', 'joao.silva@example.com', '11999998888', '2024-12-10', '2024-12-15', 101, 1500.00, 'Confirmada'),
    ('Maria Santos', 'maria.santos@example.com', '21988887777', '2024-12-12', '2024-12-17', 202, 1800.00, 'Confirmada'),
    ('Carlos Oliveira', NULL, '31977776666', '2024-12-05', '2024-12-07', 303, 600.00, 'Pendente'),
    ('Ana Costa', 'ana.costa@example.com', '41966665555', '2024-12-20', '2024-12-25', 404, 2500.00, 'Cancelada'),
    ('Luiz Pereira', 'luiz.pereira@example.com', '51955554444', '2024-12-18', '2024-12-20', 505, 800.00, 'Confirmada');


# esse é um código do terceiro dia do desafio (advent of code) sobre: criar um sistema de reservas e inserir usando query 5 novos registros usando SQL