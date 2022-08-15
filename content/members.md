---
Title: Members
__index__: true
__index_exclude__: false
---

<ul id="shuffleme">

{{#__children__}}

{{^__index_exclude__}}
<li>
<a href="members/{{__filename__}}"><b>{{Title}}</b></a>
	<em>{{role}}</em>
	<br/>
	{{#social}}
	<a href="{{url}}">
		<img height="12" src="./{{__globals__.extras_data.icon_path}}{{icon}}.svg">
		{{text}}
	</a>
	{{/social}}
	<br/><br/>
</li>
{{/__index_exclude__}}

{{/__children__}}


</ul>

{{{__globals__.extras_data.shuffle_script}}}
