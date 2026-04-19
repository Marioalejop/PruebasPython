import subprocess
import sys
import os
import time


def run_command(command, name):
    """Ejecuta un comando en consola y muestra resultado"""
    print(f"\n▶ Ejecutando {name}...")
    print(f"Comando: {' '.join(command)}\n")

    start = time.time()
    result = subprocess.run(command)
    end = time.time()

    if result.returncode == 0:
        print(f"✅ {name} PASÓ en {end - start:.2f}s\n")
    else:
        print(f"❌ {name} FALLÓ en {end - start:.2f}s\n")

    return result.returncode


def set_environment():
    """Configura variables necesarias"""
    os.environ["PYTHONPATH"] = "."


def run_smoke():
    return run_command(
        [sys.executable, "-m", "pytest", "-m", "smoke", "-v"],
        "SMOKE TESTS"
    )


def run_regression():
    return run_command(
        [sys.executable, "-m", "pytest", "-m", "regression", "-v"],
        "REGRESSION TESTS"
    )


def run_acceptance():
    return run_command(
        [sys.executable, "-m", "behave"],
        "ACCEPTANCE TESTS (BDD)"
    )


def main():
    print("\n================ PIPELINE DE PRUEBAS ================")
    print(f"🐍 Python: {sys.executable}")
    print("=====================================================\n")

    # Configurar entorno
    set_environment()

    # 1. SMOKE
    if run_smoke() != 0:
        print("🚨 Pipeline detenido por fallo en SMOKE TESTS")
        sys.exit(1)

    # 2. REGRESSION
    if run_regression() != 0:
        print("🚨 Pipeline detenido por fallo en REGRESSION TESTS")
        sys.exit(1)

    # 3. ACCEPTANCE
        print("🚨 Pipeline falló en ACCEPTANCE TESTS")
        sys.exit(1)

    print("\n🎉 PIPELINE COMPLETADO: TODOS LOS TESTS PASARON\n")


if __name__ == "__main__":
    main()