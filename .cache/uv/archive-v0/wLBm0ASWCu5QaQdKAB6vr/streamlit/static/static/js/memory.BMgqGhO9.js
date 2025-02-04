import{c as p,e as c}from"./es6.DwgrEqib.js";import"./index.Phesr84n.js";const{File:n,Blob:_,DOMException:s}=p,{INVALID:z,GONE:r,MISMATCH:w,MOD_ERR:b,SYNTAX:a,SECURITY:I,DISALLOWED:m}=c;class g{constructor(e,i){this.fileHandle=e,this.file=i,this.size=i.size,this.position=0}write(e){let i=this.file;if(typeof e=="object"){if(e.type==="write"){if(Number.isInteger(e.position)&&e.position>=0&&(this.position=e.position,this.size<e.position&&(this.file=new n([this.file,new ArrayBuffer(e.position-this.size)],this.file.name,this.file))),!("data"in e))throw new s(...a("write requires a data argument"));e=e.data}else if(e.type==="seek")if(Number.isInteger(e.position)&&e.position>=0){if(this.size<e.position)throw new s(...z);this.position=e.position;return}else throw new s(...a("seek requires a position argument"));else if(e.type==="truncate")if(Number.isInteger(e.size)&&e.size>=0){i=e.size<this.size?new n([i.slice(0,e.size)],i.name,i):new n([i,new Uint8Array(e.size-this.size)],i.name),this.size=i.size,this.position>i.size&&(this.position=i.size),this.file=i;return}else throw new s(...a("truncate requires a size argument"))}e=new _([e]);let t=this.file;const o=t.slice(0,this.position),y=t.slice(this.position+e.size);let l=this.position-o.size;l<0&&(l=0),t=new n([o,new Uint8Array(l),e,y],t.name),this.size=t.size,this.position+=e.size,this.file=t}close(){if(this.fileHandle._deleted)throw new s(...r);this.fileHandle._file=this.file,this.file=this.position=this.size=null,this.fileHandle.onclose&&this.fileHandle.onclose(this.fileHandle)}}class f{constructor(e="",i=new n([],e),t=!0){this._file=i,this.name=e,this.kind="file",this._deleted=!1,this.writable=t,this.readable=!0}async getFile(){if(this._deleted)throw new s(...r);return this._file}async createWritable(e){if(!this.writable)throw new s(...m);if(this._deleted)throw new s(...r);const i=e.keepExistingData?await this.getFile():new n([],this.name);return new g(this,i)}async isSameEntry(e){return this===e}async _destroy(){this._deleted=!0,this._file=null}}class h{constructor(e,i=!0){this.name=e,this.kind="directory",this._deleted=!1,this._entries={},this.writable=i,this.readable=!0}async*entries(){if(this._deleted)throw new s(...r);yield*Object.entries(this._entries)}async isSameEntry(e){return this===e}async getDirectoryHandle(e,i){if(this._deleted)throw new s(...r);const t=this._entries[e];if(t){if(t instanceof f)throw new s(...w);return t}else{if(i.create)return this._entries[e]=new h(e);throw new s(...r)}}async getFileHandle(e,i){const t=this._entries[e],o=t instanceof f;if(t&&o)return t;if(t&&!o)throw new s(...w);if(!t&&!i.create)throw new s(...r);if(!t&&i.create)return this._entries[e]=new f(e)}async removeEntry(e,i){const t=this._entries[e];if(!t)throw new s(...r);await t._destroy(i.recursive),delete this._entries[e]}async _destroy(e){for(let i of Object.values(this._entries)){if(!e)throw new s(...b);await i._destroy(e)}this._entries={},this._deleted=!0}}const u=new h(""),A=()=>u;export{f as FileHandle,h as FolderHandle,g as Sink,A as default};
