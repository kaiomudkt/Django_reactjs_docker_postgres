import React, { useEffect, useState } from "react";
import './style.css'
import Sidebar from "../../components/Sidebar";
import { format } from 'date-fns';
import { AiFillDelete, AiFillEdit } from "react-icons/ai";
import { useGetAllSuppliersHook } from "../../hook/supplier.hook";
// import ModalCreateCardLinks from "../../components/ModalCreateCardLinks/index";
// import FormsCreateCardLinks from '../../components/FormsCreateCardLinks';
// import FormsUpdateLink from '../../components/FormsUpdateLink';
// import FormsDeleteLink from "../../components/FormsDeleteLink";
import ModalWithContent from "../../components/ModalWithContent";

export default function AdminSupplier() {

    const [suppliers, setSuppliers] = useState([]);
    const [openModalCreateLink, setOpenModalCreateLink] = useState(false);
    const [openModalUpdate, setOpenModalUpdate] = useState(false);
    const [openModalDelete, setOpenModalDelete] = useState(false);
    const showModalCreateLink = () => setOpenModalCreateLink(!openModalCreateLink);
    const showModalUpdate = () => setOpenModalUpdate(!openModalUpdate);
    const showModalDelete = () => setOpenModalDelete(!openModalDelete);
    const [dataToEdit, setDataToEdit] = useState({})
    const [dataToDelete, setDataToDelete] = useState({})
    const getAllSuppliersApi = useGetAllSuppliersHook();
    useEffect(() => {
        try {
            async function fetchSupplier() {
                const suppliersApi = await getAllSuppliersApi({page: 1, limit: 1000})
                console.log(suppliersApi)
                setSuppliers(suppliersApi);
            }
            fetchSupplier();
        } catch (error) {
            console.log(error);
        }
    }, []);

    const execModalUpdate = (dataEntity) => {
        setDataToEdit(dataEntity);
        showModalUpdate();
    };
    const execModalDelete = (dataEntity) => {
        setDataToDelete(dataEntity);
        showModalDelete();
    };
    const ActionEdit = {
        fontSize: '25px',
        color: 'rgb(26, 26, 26)',
        cursor: 'pointer'
    };
    const ActionDelete = {
        fontSize: '25px',
        color: 'rgb(154, 17, 17)',
        cursor: 'pointer',
        marginLeft: '20px'
    };
    return (
        <>
            <Sidebar />
            <div className="container-adminLink">
                <h2>Painel administrador de Fornecedores</h2>
                <button onClick={showModalCreateLink} >Novo fornecedor</button>
                {/* <ModalCreateCardLinks isOpen={openModalCreateLink} closeModal={showModalCreateLink} content={<FormsCreateCardLinks />}> */}
                {/* </ModalCreateCardLinks> */}
                <table>
                    <thead>
                        <tr>
                            <th>Nome</th>
                            <th>Estado</th>
                            <th>CNPJ</th>
                            <th>Menu</th>
                            <th>Ações</th>
                        </tr>
                    </thead>
                    <tbody>
                        {suppliers && Object.values(suppliers).map((supplier) => {
                            return (
                                <tr key={supplier.id}>
                                    <td>{supplier.name}</td>
                                    <td>{supplier.state}</td>
                                    <td>{supplier.cnpj}</td>
                                    <td>
                                        <AiFillEdit onClick={() => execModalUpdate(supplier)} style={ActionEdit} />
                                        <ModalWithContent isOpen={openModalUpdate} closeModal={showModalUpdate}
                                            // content={<FormsUpdateLink dataEntity={dataToEdit} />}
                                        >
                                        </ModalWithContent>
                                        <AiFillDelete onClick={() => execModalDelete(supplier)} style={ActionDelete} />
                                        <ModalWithContent isOpen={openModalDelete} closeModal={showModalDelete}
                                            // content={< FormsDeleteLink dataEntity={dataToDelete} />}
                                            >
                                        </ModalWithContent>
                                    </td>
                                </tr>
                            )
                        })}
                    </tbody>
                </table>

            </div>
        </>
    )
}