import argparse
import sys

from openclaw.tasks import load_task_prompt, load_input_file
from openclaw.ollama_client import ollama_generate


def main():
    parser = argparse.ArgumentParser(
        prog="openclaw",
        description="OpenClaw learning/testing CLI"
    )

    subparsers = parser.add_subparsers(dest="command")

    # run command
    run_parser = subparsers.add_parser("run", help="Run a task")
    run_parser.add_argument("--task", required=True, help="Task name (e.g. job_analysis)")
    run_parser.add_argument("--file", required=True, help="Input file path")
    run_parser.add_argument("--model", required=True, help="Ollama model (e.g. llama3.2:1b)")
    run_parser.add_argument("--host", default="http://localhost:11434", help="Ollama host URL")

    parser.add_argument("--version", action="store_true", help="Show version")

    args = parser.parse_args()

    if args.version:
        print("openclaw 0.0.1")
        return

    if args.command == "run":
        print(f"[INFO] Running task: {args.task}")
        print(f"[INFO] Input file: {args.file}")
        print(f"[INFO] Model: {args.model}")
        print(f"[INFO] Ollama host: {args.host}")

        try:
            prompt_template = load_task_prompt(args.task)
            input_text = load_input_file(args.file)
        except Exception as e:
            print(f"[ERROR] {e}")
            sys.exit(1)

        user_prompt = (
            f"{prompt_template}\n\n"
            "----- JOB TEXT START -----\n"
            f"{input_text}\n"
            "----- JOB TEXT END -----\n"
        )

        try:
            result = ollama_generate(model=args.model, user_prompt=user_prompt, host=args.host)
        except Exception as e:
            print(f"[ERROR] Ollama call failed: {e}")
            sys.exit(2)

        print("\n<FINAL>")
        print(result)
        print("</FINAL>")
        return

    parser.print_help()


if __name__ == "__main__":
    main()
