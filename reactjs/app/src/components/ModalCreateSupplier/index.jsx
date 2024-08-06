import React from 'react'
import styled from 'styled-components';
import { AiOutlineCloseCircle } from "react-icons/ai";

const Background = styled.div`
    position: fixed;
    top: 0;
    bottom: 0;
    right: 0;
    left: 0;
    background-color: rgb(0, 0, 0, 0.7);
    z-index: 1000;
`

const ModalStyle = styled.div`
    position: fixed;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    height: 550px;
    width: 1000px;
    padding: 50px;
    background-color: #fff;
    border-radius: 10px;
    color: #2f2f2f;
`

const style = {
    fontSize: '40px',
    marginBottom: '10px',
    cursor: 'pointer',
    color: 'rgb(16, 94, 172)'
}

export default function ModalCreateSupplier({ isOpen, closeModal, content }) {

    if (isOpen) {
        return (
            <>
                <Background>
                    <ModalStyle>
                        <AiOutlineCloseCircle style={style} onClick={closeModal} />
                        {content}
                    </ModalStyle>
                </Background>
            </>
        )
    }

    return null;

}
