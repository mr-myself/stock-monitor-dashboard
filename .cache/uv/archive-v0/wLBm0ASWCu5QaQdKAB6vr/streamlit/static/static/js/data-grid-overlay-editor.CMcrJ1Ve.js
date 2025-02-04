import{r,b as $}from"./index.Phesr84n.js";import{s as z,i as w,a as J,b as Q,T as U,C as Z,m as ee}from"./index.Cx96tybK.js";import"./FormClearHelper.DwtQkhSE.js";import"./withFullScreenWrapper.BE5Y_29x.js";import"./Toolbar.BZTRaRnq.js";import"./sprintf.C-r3gIuM.js";import"./createDownloadLinkElement.DZMwyjvU.js";import"./slicedToArray.Dw1BZbJJ.js";import"./getPrototypeOf.BipnGiky.js";import"./createSuper.CU_8JFKo.js";import"./FileDownload.esm.D59tnQTx.js";const te=()=>t=>t.targetX,re=()=>t=>t.targetY,ie=()=>t=>t.targetWidth,ne=()=>t=>t.targetHeight,se=()=>t=>t.targetY+10,ae=()=>t=>Math.max(0,(t.targetHeight-28)/2),oe=z("div")({name:"DataGridOverlayEditorStyle",class:"gdg-d19meir1",propsAsIs:!1,vars:{"d19meir1-0":[re(),"px"],"d19meir1-1":[te(),"px"],"d19meir1-2":[ie(),"px"],"d19meir1-3":[ne(),"px"],"d19meir1-4":[se(),"px"],"d19meir1-5":[ae(),"px"]}});function de(){const[t,s]=r.useState();return[t??void 0,s]}function le(){const[t,s]=de(),[n,y]=r.useState(0),[g,x]=r.useState(!0);r.useLayoutEffect(()=>{if(t===void 0||!("IntersectionObserver"in window))return;const a=new IntersectionObserver(o=>{o.length!==0&&x(o[0].isIntersecting)},{threshold:1});return a.observe(t),()=>a.disconnect()},[t]),r.useEffect(()=>{if(g||t===void 0)return;let a;const o=()=>{const{right:S}=t.getBoundingClientRect();y(p=>Math.min(p+window.innerWidth-S-10,0)),a=requestAnimationFrame(o)};return a=requestAnimationFrame(o),()=>{a!==void 0&&cancelAnimationFrame(a)}},[t,g]);const O=r.useMemo(()=>({transform:`translateX(${n}px)`}),[n]);return{ref:s,style:O}}const xe=t=>{const{target:s,content:n,onFinishEditing:y,forceEditMode:g,initialValue:x,imageEditorOverride:O,markdownDivCreateNode:a,highlight:o,className:S,theme:p,id:H,cell:v,bloom:c,validateCell:d,getCellRenderer:F,provideEditor:h,isOutsideClick:X}=t,[l,A]=r.useState(g?n:void 0),k=r.useRef(l??n);k.current=l??n;const[E,R]=r.useState(()=>d===void 0?!0:!(w(n)&&(d==null?void 0:d(v,n,k.current))===!1)),f=r.useCallback((e,i)=>{y(E?e:void 0,i)},[E,y]),K=r.useCallback(e=>{if(d!==void 0&&e!==void 0&&w(e)){const i=d(v,e,k.current);i===!1?R(!1):(typeof i=="object"&&(e=i),R(!0))}A(e)},[v,d]),C=r.useRef(!1),m=r.useRef(void 0),W=r.useCallback(()=>{f(l,[0,0]),C.current=!0},[l,f]),Y=r.useCallback((e,i)=>{f(e,i??m.current??[0,0]),C.current=!0},[f]),j=r.useCallback(async e=>{let i=!1;e.key==="Escape"?(e.stopPropagation(),e.preventDefault(),m.current=[0,0]):e.key==="Enter"&&!e.shiftKey?(e.stopPropagation(),e.preventDefault(),m.current=[0,1],i=!0):e.key==="Tab"&&(e.stopPropagation(),e.preventDefault(),m.current=[e.shiftKey?-1:1,0],i=!0),window.setTimeout(()=>{!C.current&&m.current!==void 0&&(f(i?l:void 0,m.current),C.current=!0)},0)},[f,l]),D=l??n,[u,q]=r.useMemo(()=>{var i,G;if(J(n))return[];const e=h==null?void 0:h(n);return e!==void 0?[e,!1]:[(G=(i=F(n))==null?void 0:i.provideEditor)==null?void 0:G.call(i,n),!1]},[n,F,h]),{ref:B,style:L}=le();let P=!0,M,_=!0,b;if(u!==void 0){P=u.disablePadding!==!0,_=u.disableStyling!==!0;const e=Q(u);e&&(b=u.styleOverride);const i=e?u.editor:u;M=r.createElement(i,{isHighlighted:o,onChange:K,value:D,initialValue:x,onFinishedEditing:Y,validatedSelection:w(D)?D.selectionRange:void 0,forceEditMode:g,target:s,imageEditorOverride:O,markdownDivCreateNode:a,isValid:E,theme:p})}b={...b,...L};const N=document.getElementById("portal");if(N===null)return console.error('Cannot open Data Grid overlay editor, because portal not found.  Please add `<div id="portal" />` as the last child of your `<body>`.'),null;let I=_?"gdg-style":"gdg-unstyle";E||(I+=" gdg-invalid"),P&&(I+=" gdg-pad");const T=(c==null?void 0:c[0])??1,V=(c==null?void 0:c[1])??1;return $.createPortal(r.createElement(U.Provider,{value:p},r.createElement(Z,{style:ee(p),className:S,onClickOutside:W,isOutsideClick:X},r.createElement(oe,{ref:B,id:H,className:I,style:b,as:q===!0?"label":void 0,targetX:s.x-T,targetY:s.y-V,targetWidth:s.width+T*2,targetHeight:s.height+V*2},r.createElement("div",{className:"gdg-clip-region",onKeyDown:j},M)))),N)};export{xe as default};
