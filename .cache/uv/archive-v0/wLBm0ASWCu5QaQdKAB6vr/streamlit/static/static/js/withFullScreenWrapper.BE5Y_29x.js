import{n as m,r as n,a6 as x,aQ as p,M as y,j as i,aw as C}from"./index.Phesr84n.js";const h=m("div",{target:"e12yskxj0"})(({theme:e,isExpanded:t})=>({...t?{position:"fixed",top:0,left:0,bottom:0,right:0,background:e.colors.bgColor,zIndex:e.zIndices.fullscreenWrapper,padding:e.spacing.md,paddingTop:e.sizes.fullScreenHeaderHeight,overflow:["auto","overlay"],display:"flex",alignItems:"center",justifyContent:"center"}:{}})),f=n.createContext(null);f.displayName="ElementFullscreenContext";const w=e=>{const t=n.useContext(e);if(t==null)throw new Error(`useRequiredContext: ${e.displayName??"context"} not found`);return t},F=()=>{const{setFullScreen:e}=n.useContext(x),[t,s]=n.useState(!1),{fullHeight:d,fullWidth:o}=w(p),l=n.useCallback(u=>{s(u),e(u)},[e]),c=n.useCallback(()=>{document.body.style.overflow="hidden",l(!0)},[l]),r=n.useCallback(()=>{document.body.style.overflow="unset",l(!1)},[l]),a=n.useCallback(u=>{u.keyCode===27&&t&&r()},[r,t]);return n.useEffect(()=>(document.addEventListener("keydown",a,!1),()=>{document.removeEventListener("keydown",a,!1)}),[a]),n.useMemo(()=>({expanded:t,zoomIn:c,zoomOut:r,fullHeight:d,fullWidth:o}),[t,c,r,d,o])},S=({children:e,height:t,width:s})=>{const d=y(),{expanded:o,fullHeight:l,fullWidth:c,zoomIn:r,zoomOut:a}=F(),u=n.useMemo(()=>({width:o?c:s,height:o?l:t,expanded:o,expand:r,collapse:a}),[o,l,c,t,s,r,a]);return i(f.Provider,{value:u,children:i(h,{isExpanded:o,"data-testid":"stFullScreenFrame",theme:d,children:e})})};function v(e){const t=s=>i(S,{width:s.width,children:i(e,{...s})});return t.displayName=`withFullScreenWrapper(${e.displayName||e.name})`,C(t,e)}export{f as E,w as u,v as w};
