import{R as B,a6 as h,aG as i,j as e,aH as p,aY as w,aF as D,aI as b}from"./index.Phesr84n.js";import{c as k}from"./createDownloadLinkElement.DZMwyjvU.js";function R(n,a,t){return k({enforceDownloadInNewTab:t,url:n.buildMediaURL(a),filename:""})}function y(n){const{disabled:a,element:t,widgetMgr:s,width:l,endpoints:d,fragmentId:r}=n,c={width:l},{libConfig:{enforceDownloadInNewTab:u=!1}}=B.useContext(h);let o=i.SECONDARY;t.type==="primary"?o=i.PRIMARY:t.type==="tertiary"&&(o=i.TERTIARY);const f=()=>{s.setTriggerValue(t,{fromUi:!0},r),R(d,t.url,u).click()},m=t.help?l:!0;return e("div",{className:"stDownloadButton","data-testid":"stDownloadButton",style:c,children:e(p,{help:t.help,children:e(w,{kind:o,size:D.SMALL,disabled:a,onClick:f,fluidWidth:t.useContainerWidth?m:!1,children:e(b,{icon:t.icon,label:t.label})})})})}export{y as default};
