# Python Project Template

Add your description here

## Features

- **Dask** distributed computing
- **Loguru** structured logging
- **Ruff** linting and formatting
- **UV** package management
- **Click** CLI support
- **pydub** audio processing

## Installation

### 使用 Copier 克隆模板

1. **从 Git 仓库克隆模板:**

   ```bash
   copier copy <template-source> py-project-template
   ```

2. **从本地目录克隆模板:**

   ```bash
   copier copy /path/to/local/template py-project-template
   ```

3. **安装依赖:**
   ```bash
   cd py-project-template
   uv sync
   ```

### 主要功能

- **Dask** 分布式计算
- **Loguru** 结构化日志
- **Ruff** 代码检查和格式化
- **UV** 包管理
- **Click** CLI 支持

## Usage

### Development

```bash
# Start the development server
make dev
```

## Project Structure

```
py-project-template/
├── config/
│   └── config.yaml          # Configuration file
├── src/
│   ├── __init__.py
│   ├── app.py              # Main application logic
│   ├── main.py             # Entry point
│   └── utils/              # Utility modules
│       ├── __init__.py
│       ├── config.py       # Configuration management
│       ├── custom_logging.py
│       ├── dask.py         # Dask utilities
│       └── utils.py
├── Makefile                # Common commands
├── pyproject.toml          # Project configuration
├── copier.yml              # Template configuration
└── README.md               # This file
```

## Configuration

The configuration is managed through `config/config.yaml`:

- **HTTP Server**: Port 13000
- **Dask Cluster**: Scheduler port 8786, Dashboard port 8787
- **Logging**: Level INFO, rotation 1 days, retention 5 days

## Development

### Code Quality

```bash
# Lint code
uv run ruff check .

# Format code
uv run ruff format .
```

### Testing

To enable testing, set `include_tests: true` when generating the project.

## Template Variables

This template uses the following variables:

| Variable              | Description          | Default                     |
| --------------------- | -------------------- | --------------------------- |
| `project_name`        | Project name         | `py-project-template`       |
| `project_description` | Project description  | `Add your description here` |
| `author_name`         | Author name          | `""`                        |
| `author_email`        | Author email         | `""`                        |
| `python_version`      | Python version       | `3.12`                      |
| `use_dask`            | Enable Dask          | `true`                      |
| `use_click`           | Enable Click CLI     | `true`                      |
| `http_port`           | HTTP server port     | `13000`                     |
| `dask_scheduler_port` | Dask scheduler port  | `8786`                      |
| `dask_dashboard_port` | Dask dashboard port  | `8787`                      |
| `log_level`           | Logging level        | `INFO`                      |
| `log_rotation`        | Log rotation period  | `1 days`                    |
| `log_retention`       | Log retention period | `5 days`                    |

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Acknowledgments

- [Copier](https://copier.readthedocs.io/) for project templating
- [Dask](https://dask.org/) for distributed computing
- [UV](https://docs.astral.sh/uv/) for package management
- [Ruff](https://github.com/astral-sh/ruff) for linting and formatting
