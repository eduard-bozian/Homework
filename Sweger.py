openapi: 3.0.0
info:
  title: Taskmanager API
  version: 1.0.0
servers:
  - url: http://localhost:8000
paths:
  /:
    get:
      summary: Welcome
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
  /task/:
    get:
      summary: All Tasks
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/Task'
    post:
      summary: Create Task
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateTask'
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
  /task/{task_id}:
    get:
      summary: Task By Id
      parameters:
        - in: path
          name: task_id
          required: true
          schema:
            type: integer
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
    put:
      summary: Update Task
      parameters:
        - in: path
          name: task_id
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateTask'
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Task'
    delete:
      summary: Delete Task
      parameters:
        - in: path
          name: task_id
          required: true
          schema:
            type: integer
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
  /user/:
    get:
      summary: All Users
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/User'
    post:
      summary: Create User
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateUser'
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
  /user/{user_id}:
    get:
      summary: User By Id
      parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
    put:
      summary: Update User
      parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UpdateUser'
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/User'
    delete:
      summary: Delete User
      parameters:
        - in: path
          name: user_id
          required: true
          schema:
            type: integer
      responses:
        200:
          description: OK
          content:
            application/json:
              schema:
                type: object
                properties:
                  message:
                    type: string
components:
  schemas:
    Task:
      type: object
      properties:
        id:
          type: integer
        title:
          type: string
        content:
          type: string
        priority:
          type: integer
    CreateTask:
      type: object
      properties:
        title:
          type: string
        content:
          type: string
        priority:
          type: integer
    UpdateTask:
      type: object
      properties:
        title:
          type: string
        content:
          type: string
        priority:
          type: integer
    User:
      type: object
      properties:
        id:
          type: integer
        username:
          type: string
        firstname:
          type: string
        lastname:
          type: string
        age:
          type: integer
    CreateUser:
      type: object
      properties:
        username:
          type: string
        firstname:
          type: string
        lastname:
          type: string
        age:
          type: integer
    UpdateUser:
      type: object
      properties:
        firstname:
          type: string
        lastname:
          type: string
        age:
          type: integer
