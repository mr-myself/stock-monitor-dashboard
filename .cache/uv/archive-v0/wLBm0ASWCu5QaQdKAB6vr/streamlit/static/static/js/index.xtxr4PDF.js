import{n as l,a8 as g,j as o}from"./index.Phesr84n.js";import{S as m,T as y}from"./Toolbar.BZTRaRnq.js";import{w as h,u as W,E as F}from"./withFullScreenWrapper.BE5Y_29x.js";const b=l("div",{target:"e1wa958q0"})(({theme:t})=>({display:"flex",flexDirection:"row",flexWrap:"wrap",rowGap:t.spacing.lg,maxWidth:"100%",width:"fit-content"})),O=l("div",{target:"e1wa958q1"})({display:"flex",flexDirection:"column",alignItems:"stretch",width:"auto",flexGrow:0}),E=l("div",{target:"e1wa958q2"})(({theme:t})=>({fontFamily:t.genericFonts.bodyFont,fontSize:t.fontSizes.sm,color:t.colors.fadedText60,textAlign:"center",marginTop:t.spacing.xs,wordWrap:"break-word",padding:t.spacing.threeXS}));var p;(function(t){t[t.OriginalWidth=-1]="OriginalWidth",t[t.ColumnWidth=-2]="ColumnWidth",t[t.AutoWidth=-3]="AutoWidth",t[t.MinImageOrContainer=-4]="MinImageOrContainer",t[t.MaxImageOrContainer=-5]="MaxImageOrContainer"})(p||(p={}));function M({element:t,width:u,endpoints:f,disableFullscreenMode:x}){const{expanded:a,width:w,height:r,expand:C,collapse:I}=W(F),d=a?w:u;let i;const n=t.width;if([-1,-3,-4].includes(n))i=void 0;else if([-2,-5].includes(n))i=d;else if(n>0)i=n;else throw Error(`Invalid image width: ${n}`);const e={};return r&&a?(e.maxHeight=r,e.objectFit="contain"):(e.width=i,e.maxWidth="100%"),g(m,{width:d,height:r,useContainerWidth:a,topCentered:!0,children:[o(y,{target:m,isFullScreen:a,onExpand:C,onCollapse:I,disableFullscreenMode:x}),o(b,{className:"stImage","data-testid":"stImage",children:t.imgs.map((S,c)=>{const s=S;return g(O,{"data-testid":"stImageContainer",children:[o("img",{style:e,src:f.buildMediaURL(s.url),alt:c.toString()}),s.caption&&o(E,{"data-testid":"stImageCaption",style:e,children:` ${s.caption} `})]},c)})})]})}const L=h(M);export{L as default};
