import{r as i,A as h}from"./index.Phesr84n.js";import{u as p}from"./FormClearHelper.DwtQkhSE.js";function v({getStateFromWidgetMgr:e,getDefaultState:c,updateWidgetMgrState:l,element:s,widgetMgr:u,fragmentId:t,onFormCleared:r}){const[n,V]=i.useState(()=>e(u,s)??c(u,s)),[f,a]=i.useState({value:n,fromUi:!1});i.useEffect(()=>{h(f)||(a(null),V(f.value),l(s,u,f,t))},[f,l,s,u,t]);const o=i.useCallback(()=>{a({value:c(u,s),fromUi:!0}),r==null||r()},[a,s,c,u,r]);return p({widgetMgr:u,element:s,onFormCleared:o}),[n,a]}function E({getStateFromWidgetMgr:e,getDefaultStateFromProto:c,getCurrStateFromProto:l,updateWidgetMgrState:s,element:u,widgetMgr:t,fragmentId:r,onFormCleared:n}){const V=i.useCallback((o,x)=>c(x),[c]),[f,a]=v({getStateFromWidgetMgr:e,getDefaultState:V,updateWidgetMgrState:s,element:u,widgetMgr:t,fragmentId:r,onFormCleared:n});return i.useEffect(()=>{u.setValue&&(u.setValue=!1,a({value:l(u),fromUi:!1}))},[u,l,a]),[f,a]}export{E as a,v as u};
