"""
The Facade Design Pattern is a structural design pattern that provides a single,
simplified interface to a complex subsystem. Instead of forcing clients to 
coordinate many moving parts, a facade hides the internal complexity and exposes
a clean, easy-to-use entry point.
"""


import sys
import time

class VersionControlSystem:
   def pull_latest_changes(self, branch):
       print(f"VCS: Pulling latest changes from '{branch}'...")
       self._simulate_delay()
       print("VCS: Pull complete.")

   def _simulate_delay(self):
       time.sleep(1)

class BuildSystem:
   def compile_project(self):
       print("BuildSystem: Compiling project...")
       self._simulate_delay(2)
       print("BuildSystem: Build successful.")
       return True

   def get_artifact_path(self):
       path = "target/myapplication-1.0.jar"
       print(f"BuildSystem: Artifact located at {path}")
       return path

   def _simulate_delay(self, seconds):
       time.sleep(seconds)

class TestingFramework:
   def run_unit_tests(self):
       print("Testing: Running unit tests...")
       self._simulate_delay(1.5)
       print("Testing: Unit tests passed.")
       return True

   def run_integration_tests(self):
       print("Testing: Running integration tests...")
       self._simulate_delay(3)
       print("Testing: Integration tests passed.")
       return True

   def _simulate_delay(self, seconds):
       time.sleep(seconds)

class DeploymentTarget:
   def transfer_artifact(self, artifact_path, server):
       print(f"Deployment: Transferring {artifact_path} to {server}...")
       self._simulate_delay(1)
       print("Deployment: Transfer complete.")

   def activate_new_version(self, server):
       print(f"Deployment: Activating new version on {server}...")
       self._simulate_delay(0.5)
       print(f"Deployment: Now live on {server}!")

   def _simulate_delay(self, seconds):
       time.sleep(seconds)

class DeploymentClient:
    @staticmethod
    def main() -> None:
        branch = "main"
        prod_server = "prod.server.example.com"

        # Client must create and manage all subsystems
        vcs = VersionControlSystem()
        build_system = BuildSystem()
        test_framework = TestingFramework()
        deploy_target = DeploymentTarget()

        print(f"\n[Client] Starting deployment for branch: {branch}")

        # Step 1: Pull latest code
        vcs.pull_latest_changes(branch)

        # Step 2: Build the project
        if not build_system.compile_project():
            print("[Client] Build failed. Deployment aborted.", file=sys.stderr)
            return
        artifact = build_system.get_artifact_path()

        # Step 3: Run tests
        if not test_framework.run_unit_tests():
            print("[Client] Unit tests failed. Deployment aborted.", file=sys.stderr)
            return
        if not test_framework.run_integration_tests():
            print("[Client] Integration tests failed. Deployment aborted.", file=sys.stderr)
            return

        # Step 4: Deploy to production
        deploy_target.transfer_artifact(artifact, prod_server)
        deploy_target.activate_new_version(prod_server)

        print("[Client] Deployment successful!")


"""

The Facade Pattern introduces a high-level interface that hides the complexities 
of one or more subsystems and exposes only the functionality needed by the client.
"""

class DeploymentFacade:
   def __init__(self):
       self.vcs = VersionControlSystem()
       self.build_system = BuildSystem()
       self.testing_framework = TestingFramework()
       self.deployment_target = DeploymentTarget()

   def deploy_application(self, branch, server_address):
       print(f"\nFACADE: --- Initiating FULL DEPLOYMENT for branch: {branch} to {server_address} ---")
       success = True

       try:
           self.vcs.pull_latest_changes(branch)

           if not self.build_system.compile_project():
               print("FACADE: DEPLOYMENT FAILED - Build compilation failed.", file=sys.stderr)
               return False

           artifact_path = self.build_system.get_artifact_path()

           if not self.testing_framework.run_unit_tests():
               print("FACADE: DEPLOYMENT FAILED - Unit tests failed.", file=sys.stderr)
               return False

           if not self.testing_framework.run_integration_tests():
               print("FACADE: DEPLOYMENT FAILED - Integration tests failed.", file=sys.stderr)
               return False

           self.deployment_target.transfer_artifact(artifact_path, server_address)
           self.deployment_target.activate_new_version(server_address)

           print(f"FACADE: APPLICATION DEPLOYED SUCCESSFULLY to {server_address}!")
       except Exception as e:
           print(f"FACADE: DEPLOYMENT FAILED - An unexpected error occurred: {str(e)}", file=sys.stderr)
           import traceback
           traceback.print_exc()
           success = False

       return success
   
class DeploymentAppFacade:
   @staticmethod
   def main():
       deployment_facade = DeploymentFacade()

       # Deploy to production
       deployment_facade.deploy_application("main", "prod.server.example.com")

       # Deploy a feature branch to staging
       print("\n--- Deploying feature branch to staging ---")
       deployment_facade.deploy_application("feature/new-ui", "staging.server.example.com")

if __name__ == "__main__":
   DeploymentAppFacade.main()