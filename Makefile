.PHONY: dev
dev: check-dev
dev: BINDIP := 0.0.0.0
dev: BINDPORTS := 8087:8080
dev: ARGS := -v $(PROV_DIR_PATH):/build -e DB_HOST=$(DB_HOST) -e PORT0=8080 -e DEBUG=True -e PORT1=5432 -e DB_STUNNEL_HOST=$(DB_HOST) -e DB_USER=postgres -e DB_NAME=dev_cfp -e SSL_CA_HOST=$(SSL_CA_HOST) -e SSL_CA_API_KEY=$(SSL_CA_API_KEY)
dev: run
dev: exec-dev

.PHONY: delpoy
deploy: MARATHON = https://misc.marathon.in.pdx.cfdata.org/v2/groups
deploy: MARATHON_FILE := prod.yaml
deploy: upload

.PHONY: preflight 
preflight:
	./scripts/preflight.sh	


.PHONY: mongo
mongo: preflight
	docker run --name mongo1 -d  -v `pwd`:/state mongo

.PHONY: bootstrap
bootstrap: 
	docker exec -it mongo1 mongoimport --db test --collection restaurants --drop --file /state/primer-dataset.json

.PHONY: datasource
datasource: mongo bootstrap

.PHONY: run-web
run-web:
	MONGO_LOCATION=`docker inspect --format '{{ .NetworkSettings.IPAddress }}' mongo1` python web.py


