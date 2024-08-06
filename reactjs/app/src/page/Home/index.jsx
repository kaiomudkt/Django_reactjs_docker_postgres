import React, { useEffect } from "react";
import Sidebar from "../../components/Sidebar";
import styled from "styled-components";

const Info = styled.div`
    width: calc(100% - 250px);
    position: absolute;
    right: 0;
    display: flex;
    height: 70vh;
    align-items: center;
    justify-content: center;
    font-size: 130px;
    font-family: sans-serif;
    font-weight: bold;
    color: rgb(220 220 227);
`

export default function Home () {


    return(
        <>
            <Sidebar></Sidebar>
            <Info>Clarke</Info>
        </>
    )
}