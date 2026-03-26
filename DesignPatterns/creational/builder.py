"""
The builder design pattern is a creational pattern thats let you construct complex objects
step by step, separating the construction logic from the final reprsentation.

It is usually useful when
 - object has many optional fields
 - avoid telescoping constructors
 - the object must be assembled through multiple steps, possible in a specific order

"""

class HttpRequestTelescoping:
    def __init__(self, url, method="GET", headers=None, query_params=None, body=None, timeout=30000):
        self.url = url
        self.method = method
        self.headers = headers if headers is not None else {}
        self.query_params = query_params if query_params is not None else {}
        self.body = body
        self.timeout = timeout

        print(f"HttpRequest Created: URL={url}, "
              f"Method={method}, "
              f"Headers={len(self.headers)}, "
              f"Params={len(self.query_params)}, "
              f"Body={body is not None}, "
              f"Timeout={timeout}")

    # Optional: add getter methods if needed


"""
1. Hard to read or write
2. Error-prone
3. inflexible and fragile
4. poor scalability

The Builder pattern involves four participants. In many real-world implemntations
the director is optional is often skipped using fluent builders.

- Director
- Interface
- Builder
- Product

"""

class HttpRequest:

    def __init__(self, builder):
        self.url = builder._url
        self.method = builder._method
        self.headers = dict(builder._headers)
        self.query_params = dict(builder._query_params)
        self.timeout = builder._timeout
        self.body = builder._body
    
    def __str__(self):
        return (f"HttpRequest(url='{self.url}', method='{self.method}', "
                f"headers={self.headers}, query_params={self.query_params}, "
                f"body='{self.body}', timeout={self.timeout})")
    class Builder:

        def __init__(self, url):
            self._url = url  # required
            self._method = "GET"
            self._headers = {}
            self._query_params = {}
            self._body = None
            self._timeout = 30000

        def method(self, method):
            self._method = method
            return self

        def add_header(self,key, value):
            self._headers[key] = value
            return self

        def add_query_param(self, key, value):
            self._query_params[key] = value
            return self
        
        def body(self, body):
            self._body = body
            return self
        
        def timeout(self, timeout):
            self._timeout = timeout
            return self
    
        def build(self):
            return HttpRequest(self)

class SqlQuery:
    def __init__(self, builder):
        self.table = builder._table
        self.columns = list(builder._columns)
        self.conditions = list(builder._conditions)
        self.order_by = builder._order_by
        self.order_direction = builder._order_direction
        self.limit_val = builder._limit
        self.offset_val = builder._offset

    def to_sql(self):
        cols = ", ".join(self.columns) if self.columns else "*"
        sql = f"SELECT {cols} FROM {self.table}"
        if self.conditions:
            sql += " WHERE " + " AND ".join(self.conditions)
        if self.order_by:
            sql += f" ORDER BY {self.order_by} {self.order_direction}"
        if self.limit_val > 0:
            sql += f" LIMIT {self.limit_val}"
        if self.offset_val > 0:
            sql += f" OFFSET {self.offset_val}"
        return sql

    class Builder:
        def __init__(self, table):
            self._table = table
            self._columns = []
            self._conditions = []
            self._order_by = None
            self._order_direction = "ASC"
            self._limit = 0
            self._offset = 0

        def select(self, *cols):
            self._columns.extend(cols)
            return self

        def where(self, condition):
            self._conditions.append(condition)
            return self

        def order_by(self, column, direction="ASC"):
            self._order_by = column
            self._order_direction = direction
            return self

        def limit(self, limit):
            self._limit = limit
            return self

        def offset(self, offset):
            self._offset = offset
            return self

        def build(self):
            return SqlQuery(self)

if __name__ == "__main__":
    query1 = SqlQuery.Builder("users") \
        .select("name", "email") \
        .where("age > 18") \
        .where("active = true") \
        .order_by("name", "ASC") \
        .limit(10) \
        .build()

    query2 = SqlQuery.Builder("orders") \
        .select("id", "total", "created_at") \
        .where("status = 'completed'") \
        .where("total > 100") \
        .order_by("created_at", "DESC") \
        .limit(20) \
        .offset(40) \
        .build()

    print(query1.to_sql())
    print(query2.to_sql())

import uuid

class HttpRequestDirector:

    def build_simple_get(self, url):
        return HttpRequest.Builder(url) \
            .method("GET") \
            .timeout(30000) \
            .build()

    def build_authenticated_post(self, url, token, body):
        return HttpRequest.Builder(url) \
            .method("POST") \
            .add_header("Authorization", f"Bearer {token}") \
            .add_header("Content-Type", "application/json") \
            .body(body) \
            .timeout(10000) \
            .build()

    def build_internal_service_call(self, url):
        return HttpRequest.Builder(url) \
            .method("GET") \
            .add_header("X-Internal-Service", "true") \
            .add_header("X-Trace-Id", str(uuid.uuid4())) \
            .timeout(5000) \
            .build()

# Usage
if __name__ == "__main__":
    director = HttpRequestDirector()

    get = director.build_simple_get("https://api.example.com/users")
    post = director.build_authenticated_post(
        "https://api.example.com/orders", "token123", '{"item":"book"}')
    internal = director.build_internal_service_call(
        "https://internal.service/health")

    print(get)
    print(post)
    print(internal)

if __name__ == "__main__":
    # Simple GET request
    get = HttpRequest.Builder("https://api.example.com/users") \
        .build()

    # POST with body and custom timeout
    post = HttpRequest.Builder("https://api.example.com/users") \
        .method("POST") \
        .add_header("Content-Type", "application/json") \
        .body('{"name":"Alice","email":"alice@example.com"}') \
        .timeout(5000) \
        .build()

    # Authenticated PUT with query parameters
    put = HttpRequest.Builder("https://api.example.com/config") \
        .method("PUT") \
        .add_header("Authorization", "Bearer token123") \
        .add_header("Content-Type", "application/json") \
        .add_query_param("env", "production") \
        .add_query_param("version", "2") \
        .body('{"feature_flag":true}') \
        .timeout(10000) \
        .build()

    print(get)
    print(post)
    print(put)

    req1 = HttpRequestTelescoping("https://api.example.com/data")

    req2 = HttpRequestTelescoping(
        "https://api.example.com/submit",
        "POST",
        None,
        None,
        '{"key":"value"}'
    )

    req3 = HttpRequestTelescoping(
        "https://api.example.com/config",
        "PUT",
        {"X-API-Key": "secret"},
        None,
        "config_data",
        5000
    )
