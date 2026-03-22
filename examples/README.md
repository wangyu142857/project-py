# 示例代码目录

本目录与仓库根目录下的 `docs/` **按编号与目录名一一对应**：每个子目录只承接对应学习模块的练习代码、小 demo 与可独立运行的片段，与 `src/`（主应用）、`apps/`（完整项目）职责分离。

## 索引（集中管理）

| 子目录 | 对应文档 | 用途简述 |
|--------|----------|----------|
| `01-python-foundations` | [docs/01-python-foundations](../docs/01-python-foundations/README.md) | 语法、类型、模块、异常等基础练习 |
| `02-http-rest-auth` | [docs/02-http-rest-auth](../docs/02-http-rest-auth/README.md) | HTTP、REST、Cookie/Session/JWT 概念验证 |
| `03-fastapi` | [docs/03-fastapi](../docs/03-fastapi/README.md) | 路由、Pydantic、依赖注入等 FastAPI 片段 |
| `04-postgresql-and-sql` | [docs/04-postgresql-and-sql](../docs/04-postgresql-and-sql/README.md) | SQL 脚本、查询练习、Schema 草稿 |
| `05-sqlalchemy-and-alembic` | [docs/05-sqlalchemy-and-alembic](../docs/05-sqlalchemy-and-alembic/README.md) | ORM 模型小例、迁移实验（非生产迁移源） |
| `06-auth-and-authorization` | [docs/06-auth-and-authorization](../docs/06-auth-and-authorization/README.md) | 登录流、RBAC 等鉴权相关 demo |
| `07-security-basics` | [docs/07-security-basics](../docs/07-security-basics/README.md) | 安全主题最小复现与对照实验 |
| `08-engineering-and-testing` | [docs/08-engineering-and-testing](../docs/08-engineering-and-testing/README.md) | 日志、配置、pytest 片段 |
| `09-redis-and-celery` | [docs/09-redis-and-celery](../docs/09-redis-and-celery/README.md) | 缓存、任务队列小例 |
| `10-deployment` | [docs/10-deployment](../docs/10-deployment/README.md) | Dockerfile 草稿、本地编排片段（与 `docker/` 区分：此处为学习用） |
| `11-project-practice` | [docs/11-project-practice](../docs/11-project-practice/README.md) | 贯穿式项目中的**非正式**实验代码（正式项目放 `apps/`） |
| `12-refactoring-and-delivery` | [docs/12-refactoring-and-delivery](../docs/12-refactoring-and-delivery/README.md) | 重构对比、交付前检查清单相关脚本 |

## 约定

- 新增示例时：优先放入**编号与 `docs/` 一致**的子目录；若跨模块，以**主要学习目标**所在模块为准。
- 需要对外可运行的完整应用：放在 `apps/` 或 `src/`，此处仅保留**教学向、可丢弃**的片段。
