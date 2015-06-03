void test_spider_monkey()
{
	JSRuntime *rt;
	JSContext *cx;
	JSObject *global;
	JSClass global_class = {
	"global",0,
	JS_PropertyStub,JS_PropertyStub,JS_PropertyStub,JS_PropertyStub,
	JS_EnumerateStub,JS_ResolveStub,JS_ConvertStub,JS_FinalizeStub
	};

	/*
	* You always need:
	*        a runtime per process,
	*        a context per thread,
	*        a global object per context,
	*        standard classes (e.g. Date).
	*/
	rt = JS_NewRuntime(0x100000);
	cx = JS_NewContext(rt, 0x1000);
	global = JS_NewObject(cx, &global_class, NULL, NULL);
	JS_InitStandardClasses(cx, global);

	/*
	* Now suppose script contains some JS to evaluate, say "22/7" as a
	* bad approximation for Math.PI, or something longer, such as this:
	* "(function fact(n){if (n <= 1) return 1; return n * fact(n-1)})(5)"
	* to compute 5!
	*/
	char *script = "...";
	jsval rval;
	JSString *str;
	JSBool ok;

	ok = JS_EvaluateScript(cx, global, script, strlen(script),
	               filename, lineno, &rval);
	str = JS_ValueToString(cx, rval);
	printf("script result: %s\n", JS_GetStringBytes(str));
}
