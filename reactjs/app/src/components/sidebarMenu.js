import React, { useState } from "react";
import { Link } from "react-router-dom";
import styled from "styled-components";
import * as RiIcons from 'react-icons/ri';
import { IconContext } from "react-icons";
import tinycolor from 'tinycolor2';

const SideBarLink = styled(Link)`
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 30px;
    list-style: none;
    height: 20px;
    text-decoration: none;
    font-size: 15px;
    color: #2f2f2f;
    &:hover {
        background-image: linear-gradient(to right, #fff, rgb(128, 192, 255));
        border-right: 5px solid rgb(16, 94, 172);
    }
`

function SidebarMenu({ item, marginLeft, background, setMenuId }) {

    const [subnavOpen, setSubnavOpen] = useState(false);
    const showSubnav = () => {
        setSubnavOpen(!subnavOpen);
        item.id && setMenuId(item.id);
    };

    const linkStyle = {
        paddingLeft: `${marginLeft}px`,
        backgroundColor: `${background}`
    };


    if (item.children.length > 0) {
        const newBackground = tinycolor(background).darken(5).toString();
        return (
            <>
                <IconContext.Provider value={{ size: '20px', color: 'rgb(16, 94, 172)' }}>
                    <SideBarLink onClick={item.children && showSubnav } style={linkStyle} >
                        <div>
                            {item.name}
                        </div>
                        <div>
                            {item.children && subnavOpen ?
                                <RiIcons.RiArrowUpSFill /> : <RiIcons.RiArrowDownSFill />
                            }
                        </div>
                    </SideBarLink>
                    {subnavOpen && item.children.map((nextchildren, index) => {
                        return (
                            <SidebarMenu setMenuId={setMenuId} key={index} item={nextchildren} marginLeft={marginLeft + 20} background={newBackground} />
                        )
                    })}
                </IconContext.Provider>
            </>
        )
    } else {
        return (
            <>
                <IconContext.Provider value={{ size: '20px', color: 'rgb(16, 94, 172)' }}>
                    <SideBarLink onClick={item.children && showSubnav} style={linkStyle} >
                        <div>
                            {item.name}
                        </div>
                    </SideBarLink>
                </IconContext.Provider>
            </>
        )
    }
}

export default SidebarMenu;
