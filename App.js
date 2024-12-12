import React, { useState } from 'react';

function App() {
  const [items, setItems] = useState([]);
  const [inputValue, setInputValue] = useState('');

  // Adiciona um novo item
  const addItem = () => {
    if (inputValue.trim()) {
      setItems([...items, inputValue.trim()]);
      setInputValue('');
    }
  };

  // Remove um item da lista
  const removeItem = (index) => {
    setItems(items.filter((_, i) => i !== index));
  };

  return (
    <div style={{ margin: '20px', fontFamily: 'Arial, sans-serif' }}>
      <h1>Lista de Itens</h1>
      <div style={{ marginBottom: '10px' }}>
        <input
          type="text"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="Digite um item"
          style={{
            padding: '8px',
            width: '200px',
            marginRight: '10px',
            border: '1px solid #ccc',
            borderRadius: '4px',
          }}
        />
        <button
          onClick={addItem}
          style={{
            padding: '8px 15px',
            backgroundColor: '#007bff',
            color: '#fff',
            border: 'none',
            borderRadius: '4px',
            cursor: 'pointer',
          }}
        >
          Adicionar
        </button>
      </div>

      <ul style={{ listStyleType: 'none', padding: 0 }}>
        {items.map((item, index) => (
          <li
            key={index}
            style={{
              marginBottom: '8px',
              padding: '8px',
              backgroundColor: '#f9f9f9',
              border: '1px solid #ddd',
              borderRadius: '4px',
              display: 'flex',
              justifyContent: 'space-between',
              alignItems: 'center',
            }}
          >
            {item}
            <button
              onClick={() => removeItem(index)}
              style={{
                padding: '5px 10px',
                backgroundColor: '#dc3545',
                color: '#fff',
                border: 'none',
                borderRadius: '4px',
                cursor: 'pointer',
              }}
            >
              Remover
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;