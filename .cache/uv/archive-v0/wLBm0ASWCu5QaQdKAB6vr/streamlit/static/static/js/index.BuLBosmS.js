import{n as c,aE as v,Q as y,aF as l,aG as t,j as s,aH as C,aI as S}from"./index.Phesr84n.js";function k(o,a){switch(o){case l.XSMALL:return{padding:`${a.spacing.twoXS} ${a.spacing.sm}`,fontSize:a.fontSizes.sm};case l.SMALL:return{padding:`${a.spacing.twoXS} ${a.spacing.md}`};case l.LARGE:return{padding:`${a.spacing.md} ${a.spacing.md}`};default:return{padding:`${a.spacing.xs} ${a.spacing.md}`}}}const g=c("a",{target:"eeng2fo0"})(({fluidWidth:o,size:a,theme:r})=>{const i=typeof o=="number"?`${o}px`:"100%";return{display:"inline-flex",alignItems:"center",justifyContent:"center",fontWeight:r.fontWeights.normal,padding:`${r.spacing.xs} ${r.spacing.md}`,borderRadius:r.radii.default,minHeight:r.sizes.minElementHeight,margin:0,lineHeight:r.lineHeights.base,color:r.colors.primary,textDecoration:"none",width:o?i:"auto",userSelect:"none","&:visited":{color:r.colors.primary},"&:focus":{outline:"none"},"&:focus-visible":{boxShadow:`0 0 0 0.2rem ${y(r.colors.primary,.5)}`},"&:hover":{textDecoration:"none"},"&:active":{textDecoration:"none"},...k(a,r)}}),B=c(g,{target:"eeng2fo1"})(({theme:o})=>({backgroundColor:o.colors.primary,color:o.colors.white,border:`${o.sizes.borderWidth} solid ${o.colors.primary}`,"&:hover":{backgroundColor:v(o.colors.primary,.05),color:o.colors.white},"&:active":{backgroundColor:"transparent",color:o.colors.primary},"&:visited:not(:active)":{color:o.colors.white},"&[disabled], &[disabled]:hover, &[disabled]:active, &[disabled]:visited":{borderColor:o.colors.borderColor,backgroundColor:o.colors.transparent,color:o.colors.fadedText40,cursor:"not-allowed"}})),x=c(g,{target:"eeng2fo2"})(({theme:o})=>({backgroundColor:o.colors.lightenedBg05,color:o.colors.bodyText,border:`${o.sizes.borderWidth} solid ${o.colors.borderColor}`,"&:visited":{color:o.colors.bodyText},"&:hover":{borderColor:o.colors.primary,color:o.colors.primary},"&:active":{color:o.colors.white,borderColor:o.colors.primary,backgroundColor:o.colors.primary},"&:focus:not(:active)":{borderColor:o.colors.primary,color:o.colors.primary},"&[disabled], &[disabled]:hover, &[disabled]:active":{borderColor:o.colors.borderColor,backgroundColor:o.colors.transparent,color:o.colors.fadedText40,cursor:"not-allowed"}})),$=c(g,{target:"eeng2fo3"})(({theme:o})=>({padding:o.spacing.none,backgroundColor:o.colors.transparent,color:o.colors.bodyText,border:"none","&:visited":{color:o.colors.bodyText},"&:hover":{color:o.colors.primary},"&:active":{color:o.colors.primary},"&:focus":{outline:"none"},"&:focus-visible":{color:o.colors.primary,boxShadow:`0 0 0 0.2rem ${y(o.colors.primary,.5)}`},"&[disabled], &[disabled]:hover, &[disabled]:active":{backgroundColor:o.colors.transparent,color:o.colors.fadedText40,cursor:"not-allowed"}}));function L({kind:o,size:a,disabled:r,fluidWidth:i,children:d,autoFocus:n,href:e,rel:u,target:p,onClick:f}){let b=B;return o===t.SECONDARY?b=x:o===t.TERTIARY&&(b=$),s(b,{kind:o,size:a||l.MEDIUM,fluidWidth:i||!1,disabled:r||!1,autoFocus:n||!1,href:e,target:p,rel:u,onClick:f,tabIndex:r?-1:0,"data-testid":`stBaseLinkButton-${o}`,children:d})}function T(o){const{disabled:a,element:r,width:i}=o,d={width:i};let n=t.SECONDARY;r.type==="primary"?n=t.PRIMARY:r.type==="tertiary"&&(n=t.TERTIARY);const e=r.help?i:!0,u=p=>{o.disabled&&p.preventDefault()};return s("div",{className:"stLinkButton","data-testid":"stLinkButton",style:d,children:s(C,{help:r.help,children:s(L,{kind:n,size:l.SMALL,disabled:a,onClick:u,fluidWidth:r.useContainerWidth?e:!1,href:r.url,target:"_blank",rel:"noreferrer","aria-disabled":a,children:s(S,{icon:r.icon,label:r.label})})})})}export{T as default};
