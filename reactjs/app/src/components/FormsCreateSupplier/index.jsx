import React, { useState, useEffect } from 'react'
import styled from 'styled-components';
import { useCreateSupplierHook , useGetAllSuppliersHook } from '../../hook/supplier.hook';

const Title = styled.h2`
    color: rgb(16, 94, 172);
    font-size: 28px;
    margin-bottom: 30px;
`

const Criar = styled.button`
    height: 40px;
    padding: 10px;
    border-radius: 8px;
    border: none;
    background-color: rgb(16, 94, 172);
    color: #fff;
    width: 150px;

    &:hover {
        background-color: rgb(30, 110, 191);
        cursor: pointer;
    }
`

const Upload = styled.div`
    margin-top: 20px;
`

export default function FormsCreateSupplier() {
    const [name, setName] = useState();
    const [cnpj, setCnpj] = useState();
    // const [description, setDescription] = useState();
    // const [image, setImage] = useState(); 
    const [suppliers, setSuppliers] = useState([]);
    // const [selectedMenu, setSelectedMenu] = useState();
    const saveSupplier = useCreateSupplierHook();
    const getAllSuppliersApi = useGetAllSuppliersHook();
    useEffect(() => {
        try {
            async function fetchSupplier() {
                const suppliersApi = await getAllSuppliersApi({page: 1, limit: 1000})
                setSuppliers(suppliersApi);
            }
            fetchSupplier();
        } catch (error) {
            console.log(error);
        }
    }, []);
    const handleImageChange = (event) => {
        const selectedFile = event.target.files[0];
        // setImage(selectedFile); 
    };
    const handleSave = async (event) => {
        event.preventDefault();
        if (!name || !cnpj) {
            return;
        };
        const formData = new FormData();
        formData.append('name', name);
        formData.append('cnpj', cnpj);
        // formData.append('description', description);
        // formData.append('image', image);
        await saveSupplier(formData);
        alert('sucesso!');
        window.location.reload();
    };

    return (
        <>
            <div className="content">
                <Title>Crie um novo Fornecedor de Acesso</Title>
                <form onSubmit={handleSave} encType="multipart/form-data">
                    <div className="row">
                        <label htmlFor="nome">Nome</label>
                        <input type="text" value={name} onChange={(e) => setName(e.target.value)} />
                    </div>
                    <div className="row">
                        <label htmlFor="cnpj">CNPJ</label>
                        <input type="text" value={cnpj} onChange={(e) => setCnpj(e.target.value)} />
                    </div>
                    {/* <div className="row">
                        <label htmlFor="description">Descrição</label>
                        <input type="text" value={description} onChange={(e) => setDescription(e.target.value)} />
                    </div> */}
                    {/* <div className="row">
                        <label htmlFor="image">Imagem</label>
                        <input type="file" accept=".png, .jpeg, .jpg" onChange={handleImageChange} />
                    </div> */}
                    {/* <Upload> </Upload> */}
                    {/* <div className="row">
                        <label htmlFor="menuid">Menu</label>
                        <select 
                            value={selectedMenu} 
                            onChange={(event) => setSelectedMenu(event.target.value)}
                            defaultValue={listMenus.length > 0 ? listMenus[0].id : ''}
                        >
                            <option value="" > Selecione </option>
                            {
                                listMenus.map((optionMenu) => (
                                    <option value={optionMenu.id}>
                                        {optionMenu.name}
                                    </option>
                                ))
                            }
                        </select>
                    </div> */}
                    <button type="submit">Criar</button>
                </form>
            </div>
        </>
    )
}
